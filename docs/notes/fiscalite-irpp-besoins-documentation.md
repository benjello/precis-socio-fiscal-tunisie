# Commande de documentation — IRPP (livre « Fiscalité »)

> Destinataire : agent **documentaliste** (et, pour la dernière partie, agent **bibliographe**).
> Cible rédactionnelle : section « L'impôt sur le revenu des personnes physiques (IRPP) »
> de `precis/fr/fiscalite/index.qmd` (ébauche, 49 lignes).
> Axe prioritaire demandé : **historique des barèmes de l'IRPP et textes qui les ont modifiés**,
> de la loi n° 89-114 du 30 décembre 1989 jusqu'à la LF 2026.
>
> Cette note **ne rédige pas** de prose de précis. Elle fait l'inventaire critique de l'existant,
> liste les besoins documentaires actionnables, et distingue ce qui est **déjà couvert localement**
> de ce qui est **à chercher**.
>
> Rappels de méthode du projet appliqués ici :
> — URL canonique d'un texte de loi = **JORT sur pist.tn** (jamais legislation.tn / ICJ / NATLEX en URL principale) ;
> — **aucun chiffre ponctuel isolé** : toute donnée chiffrée doit être présentée dans une série d'évolution ;
> — **attribution obligatoire** de toute appréciation à l'acteur qui la porte.

---

## 1. État des lieux de la section IRPP existante

### 1.1 Forces

- L'architecture chronologique est la bonne et correspond à la logique d'entonnoir du précis :
  héritage beylical/colonial → cédulaire 1956-1989 → code de 1989 → simplification → stabilité →
  réformes récentes.
- La partie pré-1956 est correctement sourcée sur de la littérature académique
  (`@bastier1997`, `@mesple-somps2022`) et signale sa référence de fond.
- Le fait structurant central est juste et vérifiable : le code IRPP-IS de 1989 substitue, au
  1er janvier 1990, un impôt synthétique au système mixte cédulaire + impôt général.
- La clé `loi-irpp-is-1989` existe déjà dans la bibliographie partagée
  (`precis/fr/references.json`) avec une **URL pist.tn** (`.../jort/1989/1989F/Jo08889.pdf`),
  et le PDF correspondant est présent dans le corpus local. Elle n'est cependant **jamais citée**
  dans le texte, alors que tout le paragraphe 1989-1990 en dépend.

### 1.2 Faiblesses structurelles

**(a) Mono-sourçage sur `@touaiti2026`.**
Quatre des cinq paragraphes de la chronologie 1989 → 2025 reposent sur une seule analyse de presse
(*Le Point Tunisie*) : le nombre de tranches de 1990, le taux marginal de 68 %, la simplification
de 1991, la stabilité 1991-2016, l'ajustement de 2017, la réforme de 2025. Aucun texte primaire
n'est cité à l'appui. **Aucune de ces affirmations ne peut être publiée telle quelle** avant
adossement au JORT.

**(b) Aucun barème n'est effectivement montré.**
La section parle de barèmes (nombre de tranches, taux marginal supérieur, plafonds) sans jamais
en afficher un seul. C'est précisément l'objet du travail demandé : il faut un **tableau
d'évolution des générations de barème**, pas des adjectifs sur les barèmes.

**(c) Chiffres ponctuels isolés (violation de la règle du projet).**
- « 16 tranches », « 68 % », « 6 tranches », « 35 % », « 50 000 / 80 000 dinars », « 5 000 DT »,
  « 8 tranches », « 40 % » : autant de points isolés, non replacés dans une série.
- « 18,2 % contre 16,7 % » (INS, 2023) : point unique, sans série ni définition d'assiette.

**(d) Appréciations non attribuées (à réécrire une fois documentées).**
File d'attente de réécriture pour le rédacteur — ce sont des corrections de **plume**, pas des
trous documentaires :
| Formulation actuelle | Problème | Correction attendue |
|---|---|---|
| « elle a en réalité réduit la progressivité de l'impôt et affaibli sa fonction redistributive » | jugement de Touaiti énoncé à la voix du précis, renforcé par « en réalité » | attribuer explicitement (« selon @touaiti2026… ») et, si possible, mettre en regard la justification officielle de l'époque |
| « C'est une étape charnière qui oriente la fiscalité tunisienne vers une logique d'attractivité plutôt que de redistribution » | appréciation **sans aucune citation** | attribuer ou supprimer |
| « La loi de finances 2025 a introduit une **amélioration** » | qualificatif de valeur | décrire la modification, attribuer l'appréciation |
| « une inversion de la progressivité **qui a motivé la réforme** » | causalité affirmée sur la foi d'un article de presse | rapporter la justification telle que formulée par le gouvernement (exposé des motifs / note commune), et la mesure INS séparément |
| « Si cette réforme **était présentée comme** un moyen de simplifier… » | tournure de mise en doute | exposer la justification officielle et la lecture critique en regard, sans arbitrer |

**(e) Affirmations factuellement fragiles ou contredites par les sources locales.**
- **« taux marginal maximal de 35 % pour un plafond de 50 000 dinars, contre 80 000 dinars
  auparavant » (2017)** : le chiffre de 80 000 dinars n'est corroboré par aucune source consultée.
  Les paramètres openfisca antérieurs à 2017 s'arrêtent à un seuil de 20 000 dinars, et la
  structure du barème LF 2017 (vérifiée, voir §3) ne comporte aucun palier à 80 000. **Bloquant.**
- **« 16 tranches et un taux marginal maximal de 68 % » attribués au code de 1990** : hypothèse
  de travail — ces caractéristiques pourraient décrire l'**impôt général sur le revenu (IGR)
  antérieur à 1989**, et non le barème de l'article 44 du code de 1989. À trancher sur texte.
  **Bloquant.**
- **« Le barème a été simplifié en 1991 »** : **aucun véhicule législatif n'est identifié**
  (ni numéro de loi, ni date, ni JORT). Ne pas nommer de loi candidate tant qu'elle n'est pas
  vérifiée. **Bloquant.**
- **« Entre 1991 et 2016, le barème reste largement inchangé »** : substantiable localement pour
  **2000-2016 seulement** (voir §3). La décennie **1990-1999 reste non documentée**.
- **« Un seuil d'exonération pour les bas salaires (revenu net < 5 000 DT) introduit dès la LF
  2014 »** : au moins **trois** dispositifs distincts à 5 000 dinars coexistent et sont ici
  confondus (voir question Q7). **Bloquant en l'état.**
- **« en augmentant le taux marginal supérieur à 40 % au-delà de 50 000 dinars » (LF 2025)** :
  **inexact**, vérifié sur le texte (voir §3.1). Le barème LF 2025 applique 36 % de 40 000,001 à
  50 000 D, **38 % de 50 000,001 à 70 000 D**, et **40 % seulement au-delà de 70 000 D**. Le seuil
  de 50 000 D est celui de l'ancien taux marginal (2017), pas du nouveau. **Correction immédiate.**
- La chronologie **s'arrête à la LF 2025**, alors que la LF 2026 (loi n° 2025-17 du 12 décembre
  2025) existe et comporte des dispositions IRPP (voir Q6).

**(f) Observation de périmètre (hors besoin documentaire).**
La phrase d'accroche du livre — « Ce précis a concerne les impôts en Tunisie depuis 1956 » —
comporte une coquille et contredit le contenu, qui s'ouvre sur la période beylicale et coloniale
*avant* 1956. À arbitrer par le rédacteur (élargir le périmètre annoncé ou déplacer le §
pré-1956 en « antécédents »).

---

## 2. Questions à documenter

Format : **[BLOQUANT]** = la rédaction ne peut pas avancer sans ; **[ENRICHISSEMENT]** = améliore
la section mais ne la bloque pas. Statut = *couvert localement* / *partiellement couvert* /
*à chercher*.

### Bloc A — Le barème lui-même (cœur de la commande)

**Q1. [BLOQUANT] Barème initial du code de 1989 (art. 44 §I, version d'origine) : tranches, taux, et référence JORT exacte.**
- *Question* : reproduire le tableau de l'article 44 §I tel que promulgué par la loi n° 89-114 du
  30 décembre 1989, et donner la référence JORT complète (n° du JORT, date de publication, page).
  Confirmer ou infirmer les caractéristiques « 16 tranches / taux marginal 68 % » avancées par
  `@touaiti2026`, **et** déterminer si ces caractéristiques appartiennent en réalité au régime
  antérieur (IGR).
- *Pourquoi* : c'est la colonne de départ du tableau d'évolution et le socle de tout le récit
  1989-1990. Actuellement affirmé sur la seule foi d'un article de presse.
- *Source attendue* : JORT pist.tn (le PDF est déjà local, voir §3 : `PDFs/JORT/1989/fr/Jo08889.pdf`,
  **sans couche texte → OCR requis**) ; en appui, `@ayadi1996` et `@baccouche2008` qui commentent
  le code dans sa version d'origine.
- *Statut* : **partiellement couvert** (PDF local, contenu non extrait).

**Q2. [BLOQUANT] Quel texte a modifié le barème avec effet au 1er janvier 1991 ? Quel barème en résulte ?**
- *Question* : identifier le texte (loi de finances ou autre) qui a réduit le nombre de tranches et
  abaissé le taux marginal supérieur ; en donner le numéro, la date, l'article modificatif, la
  référence JORT (n°, date, page) et le tableau de tranches/taux résultant.
- *Pourquoi* : « la simplification de 1991 » est présentée comme le tournant de la section, sans
  aucun véhicule juridique identifié.
- *Source attendue* : JORT pist.tn, décembre 1990 (édition française et arabe) ; recoupement par le
  code IRPP consolidé, qui annote les modifications successives de l'article 44.
- *Élément nouveau à verser au dossier* : le code IRPP-IS consolidé annote l'article 44 §I d'une
  **mention unique** — « (Modifié Art 14-1 LF 2016-78 du 17/12/2016) » — alors que la convention du
  même document est de dérouler la **chaîne complète** des modifications (on lit ailleurs des
  chaînes de cinq textes successifs). Deux lectures possibles, à départager : soit le §I n'a
  effectivement **jamais** été modifié entre 1990 et 2016 — auquel cas le récit d'une
  « simplification de 1991 » est à revoir de fond en comble, et le barème 1990 était déjà celui à
  six tranches —, soit la consolidation ne remonte pas au-delà de la dernière modification pour cet
  article. C'est la question centrale de la commande.
- *Statut* : **à chercher** (JORT PDF local disponible pour 1990 et 1991, sans couche texte).

**Q3. [BLOQUANT] Y a-t-il eu, entre 1991 et 2016, une ou plusieurs modifications du barème de l'article 44 §I ?**
- *Question* : établir la liste exhaustive des modifications de l'article 44 §I sur la période, ou
  attester formellement l'absence de modification.
- *Pourquoi* : l'affirmation « le barème reste largement inchangé » n'est vérifiée localement que
  pour 2000-2016. La décennie 1990-1999 est un angle mort complet (aucune LF locale pour ces
  années). Sans cela, la « longue stabilité » n'est pas publiable comme fait.
- *Source attendue* : lois de finances 1992 à 1999 (JORT pist.tn, décembre de chaque année) ;
  l'historique d'annotation du code IRPP consolidé est un raccourci efficace pour cibler les
  années à examiner.
- *Statut* : **partiellement couvert** (2000-2016 substantiable localement ; 1990-1999 à chercher).

**Q4. [BLOQUANT] Barème en vigueur *avant* le 1er janvier 2017 — le seuil du taux marginal supérieur était-il de 50 000 dinars ou de 80 000 dinars ?**
- *Question* : reproduire le barème applicable aux revenus 2016, avec sa source. Trancher la
  contradiction entre le texte du précis (80 000 D) et les paramètres openfisca (dernier seuil à
  20 000 D, sans tranche supérieure encodée).
- *Pourquoi* : chiffre publié dans la section actuelle, non corroboré, et pilier de la comparaison
  « avant/après 2017 ».
- *Source attendue* : **note commune n° 3/2017** de la DGI, qui commente l'article 14 de la LF 2017
  et reproduit conventionnellement l'ancien et le nouveau barème côte à côte. Le PDF est **local**
  mais **sans couche texte → OCR requis** (chemin en §3). À défaut : JORT de la dernière loi ayant
  fixé ce barème.
- *Statut* : **couvert localement, sous réserve d'OCR**.

**Q5. [ENRICHISSEMENT] URL pist.tn des JORT portant les barèmes 2017 et 2025.**
- *Question* : le contenu des deux barèmes **et** leurs références de publication sont établis
  localement (voir §3.1) : JORT n° 105 du 27 décembre 2016 (barème 2017) et JORT n° 149 du
  10 décembre 2024, p. 3430 (barème 2025). Il ne reste qu'à constituer les **URL pist.tn**
  correspondantes et à confirmer la pagination du barème 2017.
- *Pourquoi* : exigence de citation du projet (URL JORT pist.tn systématique).
- *Statut* : **largement couvert localement** ; seules les URL restent à produire.

**Q6. [BLOQUANT] La loi de finances 2026 (loi n° 2025-17 du 12 décembre 2025) modifie-t-elle le barème de l'IRPP ? Quelles dispositions IRPP comporte-t-elle ?**
- *Question* : (i) confirmer/infirmer toute modification de l'article 44 §I ; (ii) documenter
  l'article 91, qui semble ajouter à l'**article 44 ter** un **régime estimatif optionnel** pour
  les contribuables réalisant moins de 100 000 dinars de chiffre d'affaires (impôt forfaitaire de
  4 000 D / 5 000 D selon la classe, moitié en zones rurales, caractère libératoire, non-révision
  pendant six ans) ; (iii) référence JORT complète.
- *Pourquoi* : la section s'arrête à 2025. Si la LF 2026 ne touche pas le barème mais refond le
  régime estimatif, c'est un fait majeur pour la partie « régimes forfaitaires » et cela change la
  dernière colonne du tableau d'évolution.
- *Source attendue* : JORT pist.tn (décembre 2025) ; version **française** du texte — la seule
  version locale est en arabe. Notes communes 2026 de la DGI.
- *Statut* : **partiellement couvert** (LF 2026 locale en arabe seulement ; JORT de décembre 2025
  absent du corpus local ; lecture ci-dessus issue d'un repérage sur couche texte arabe, **à
  confirmer sur texte officiel**).

### Bloc B — Paramètres périphériques du barème

**Q7. [BLOQUANT] Démêler les dispositifs « 5 000 dinars ».**
- *Question* : distinguer et dater précisément (texte, article, JORT) :
  (i) le **seuil d'exonération** de revenu net imposable, que les paramètres openfisca datent de
  2014 **sans référence** ;
  (ii) la **tranche à 0 %** du barème jusqu'à 5 000 D, introduite par l'article 14-1 de la LF 2017 ;
  (iii) la dispense de retenue à la source sur les **rétributions provisoires ou accidentelles**
  lorsque le salaire annuel net global ne dépasse pas 5 000 D (article 14-3 de la LF 2017).
- *Pourquoi* : la phrase actuelle du précis les fusionne en un unique « seuil d'exonération
  introduit dès la LF 2014 ». Trois dispositifs différents, trois dates possiblement différentes.
- *Source attendue* : LF 2014 (loi n° 2013-54 du 30 décembre 2013) et LF 2017, JORT pist.tn ;
  notes communes DGI.
- *Statut* : **partiellement couvert** (LF 2014 et LF 2017 locales avec couche texte).

**Q8. [BLOQUANT] Déductions pour charges de famille : série des montants et textes modificatifs.**
- *Question* : construire la série datée des déductions (chef de famille, 1er à 4e enfant, enfant
  supplémentaire, enfant infirme, enfant étudiant, parent à charge) depuis 1990, avec pour chaque
  changement le texte, l'article et la référence JORT.
- *Pourquoi* : ces déductions déterminent l'impôt réellement dû et ne peuvent être publiées qu'en
  série (règle du projet). Elles sont aujourd'hui absentes de la section.
- *Point de départ* : openfisca donne des valeurs et des dates d'effet (chef de famille 150 D en
  1990 → 300 D en 2019 ; 1er enfant 90 D → 100 D en 2019 ; parent à charge 5 % du revenu depuis
  1990). **Attention** : le fichier `chef_de_famille.yaml` date l'effet au 1er janvier 2019 mais
  référence l'article 55 de la **loi n° 2017-66 (LF pour 2018)** — incohérence date/véhicule à
  trancher sur le JORT.
- *Statut* : **partiellement couvert** (valeurs à confirmer, références JORT à établir).

**Q9. [BLOQUANT] Minimum d'impôt : nature, taux, série datée.**
- *Question* : distinguer et documenter (a) le **minimum d'impôt** de l'article 44 §II (montants
  forfaitaires pour activités commerciales et non commerciales) et (b) le **plafonnement des
  déductions** (openfisca : `minimum_impot/taux` = 60 % à partir de 2014, 45 % à partir de 2020,
  sans référence). Pour chaque changement : texte, article, JORT.
- *Pourquoi* : le « minimum d'impôt » est structurant pour la charge fiscale effective des bas
  revenus et des forfaitaires, et il conditionne toute affirmation sur la progressivité effective.
- *Déjà acquis localement pour le (a)* : chaîne des modifications de l'art. 44 §II reconstituée
  (voir §3.1) — art. 42 de la LF 2006, art. 48 de la LF 2014, art. 10 de la LFC 2014
  (loi n° 2014-54 du 19 août 2014), art. 16 de la LF 2019 (loi n° 2018-56 du 27 décembre 2018) —
  et texte consolidé disponible (0,2 % du chiffre d'affaires, minimum 300 D ; 0,1 % et minimum
  200 D pour les revenus bénéficiant d'une déduction des deux tiers ou de la moitié). Restent à
  établir : les valeurs antérieures à chaque modification, et les références JORT.
- *Statut* : **largement couvert localement pour (a)** ; **à chercher pour (b)** (le plafonnement
  des déductions à 60 % puis 45 % n'a aucune référence dans openfisca et relève d'un autre article).

**Q10. [BLOQUANT] Contribution sociale de solidarité (CSS) des personnes physiques : série datée et articulation avec le barème.**
- *Question* : documenter l'instauration (art. 53 LF 2018), le passage à 0,5 point (art. 22 du
  décret-loi n° 2022-79, LF 2023, à titre temporaire pour 2023-2025), le maintien par la LF 2025,
  et **l'état du droit pour 2026** (le régime temporaire arrivait à échéance). Références JORT
  pist.tn pour chaque texte.
- *Pourquoi* : la CSS est un prélèvement adossé à l'assiette IRPP ; sans elle, le taux effectif
  présenté serait faux. Elle est absente de la section.
- *Point de départ* : openfisca documente précisément 2018 / 2023 / 2025, mais avec des URL GitLab
  privées (`tunisia-legislative-references`) comme références — **à remplacer par des URL pist.tn**.
- *Statut* : **partiellement couvert** ; le point 2026 est **à chercher**.

**Q11. [ENRICHISSEMENT] Abattements sur traitements et salaires (10 %, plafond 2 000 D ; abattement pour salaire minimum) : dates et textes.**
- *Question* : série datée de l'abattement de 10 % sur les salaires, de son plafond (2 000 D), et
  de l'abattement pour salaire minimum (openfisca : 500 D en 2005, 1 000 D en 2010, sans référence).
- *Pourquoi* : détermine l'assiette salariale ; utile au tableau des paramètres périphériques.
- *Statut* : **à chercher** (valeurs openfisca sans référence).

**Q12. [ENRICHISSEMENT] Régimes forfaitaires (art. 44 bis à 44 sexies) : chronologie des réformes.**
- *Question* : chronologie datée du régime forfaitaire BIC — conditions d'éligibilité, seuils de
  chiffre d'affaires, tarifs, mesures de retrait, jusqu'au régime estimatif optionnel de la LF 2026
  (cf. Q6).
- *Pourquoi* : sous-secteur juridique majeur de l'IRPP, mentionné nulle part dans la section, et
  central dans les débats sur l'équité fiscale entre salariés et non-salariés.
- *Déjà acquis localement* : le régime forfaitaire figurait initialement au **paragraphe IV de
  l'article 44**, avec un tarif fixé par l'**annexe II** du code ; l'**article 37 de la LF 2011**
  abroge ce §IV et l'annexe II, et transfère le dispositif à l'**article 44 bis**. Le code
  consolidé 2019-2025 porte ensuite l'historique annoté des articles 44 bis à 44 sexies.
- *Statut* : **largement couvert localement**, sauf les références JORT et le volet LF 2026 (Q6).

**Q13. [ENRICHISSEMENT] « Contribution au budget de l'État » (barème en jours de salaire, 2014).**
- *Question* : identifier le texte instituant ce prélèvement exceptionnel, sa durée d'application,
  et son abrogation éventuelle.
- *Pourquoi* : paramétré dans openfisca à partir de 2014 sans aucune référence ; utile pour ne pas
  présenter la période 2014-2016 comme fiscalement inerte.
- *Statut* : **à chercher**.

### Bloc C — Mesure et appréciations

**Q14. [BLOQUANT] La statistique INS « 18,2 % / 16,7 % » : source primaire, définition, et série.**
- *Question* : retrouver la **publication INS** d'origine (et non le relais de presse
  `@lapresse2025`) ; établir précisément (i) ce que mesure le taux d'imposition effectif — IRPP
  seul, ou ensemble des prélèvements y compris **indirects** ; (ii) l'unité d'observation (ménage,
  individu) et le classement (décile de quoi) ; (iii) l'existence d'une **série pluriannuelle** ou
  d'une ventilation par décile complète, permettant un graphique.
- *Pourquoi* : trois défauts cumulés dans la formulation actuelle. (a) chiffre ponctuel isolé,
  contraire à la règle du projet ; (b) s'il s'agit de l'incidence **totale**, en tirer une
  conclusion sur la progressivité de l'**IRPP** serait une erreur de catégorie ; (c) le lien de
  causalité avec la réforme 2025 est porté par un article de presse, pas par un document officiel.
- *Source attendue* : INS (publication et, si possible, tableau complet par décile) ; à défaut,
  microsimulation d'incidence de type CEQ (voir §3, piste `ceq-tunisie`).
- *Statut* : **à chercher**.

**Q15. [BLOQUANT] Justification officielle des réformes 2017 et 2025.**
- *Question* : recueillir la formulation par laquelle les pouvoirs publics ont justifié chacune des
  deux réformes (intitulés d'articles, exposé des motifs, notes communes DGI, communication du
  ministère des finances).
- *Pourquoi* : la règle d'attribution interdit de présenter une motivation comme un constat. Les
  intitulés officiels sont déjà partiellement identifiés localement (« Allègement de la charge
  fiscale des personnes physiques à faible revenu et renforcement de l'équité fiscale » pour 2017 ;
  « Poursuite de la réforme fiscale et renforcement des ressources du Trésor / Allègement de la
  charge fiscale des individus et renforcement de l'équité fiscale » pour 2025).
- *Statut* : **partiellement couvert**.

**Q16. [ENRICHISSEMENT] Lectures critiques attribuables, autres que `@touaiti2026`.**
- *Question* : identifier au moins deux analyses (doctrine fiscale tunisienne, organisations
  internationales, syndicats, société civile) portant sur la progressivité de l'IRPP, afin
  d'exposer des positions **en regard** plutôt qu'une seule lecture.
- *Pourquoi* : la section repose aujourd'hui sur une seule voix critique, adoptée à la voix du
  précis. Toute appréciation doit être attribuée, et la divergence entre acteurs exposée.
- *Source attendue* : `@baccouche2008`, `@ayadi1996`, `@yaich` (doctrine) ; rapports FMI/Banque
  mondiale sur la fiscalité tunisienne ; positions UGTT / UTICA sur les réformes 2017 et 2025.
- *Statut* : **à chercher**.

**Q17. [ENRICHISSEMENT] Rendement budgétaire de l'IRPP : série longue.**
- *Question* : série annuelle des recettes d'IRPP (en dinars et en % du PIB, et si possible part
  des salariés dans le total) sur une période aussi longue que possible.
- *Pourquoi* : permet de replacer les réformes de barème dans leur contexte budgétaire, et de
  respecter la règle « pas de chiffre isolé » en donnant une série de cadrage. Aucune donnée de
  rendement n'apparaît aujourd'hui dans la section.
- *Source attendue* : ministère des finances (indicateurs des finances publiques), BCT, INS.
- *Statut* : **à chercher** ; le dépôt `tunisia-data` est le point d'entrée naturel.

### Bloc D — Amont historique (moins prioritaire que le barème)

**Q18. [ENRICHISSEMENT] Le système cédulaire 1956-1989 : liste des impôts cédulaires et de l'IGR, avec leurs textes.**
- *Question* : nommer les impôts cédulaires effectivement en vigueur avant 1990 et l'impôt général
  sur le revenu qui les couronnait, avec leurs textes fondateurs et leurs dates.
- *Pourquoi* : le paragraphe correspondant repose sur une page web archivée (`@eset2016`), source
  secondaire faible pour une affirmation de droit positif. C'est aussi le moyen de trancher Q1
  (le « 68 % » appartient-il à l'IGR ?).
- *Source attendue* : JORT pist.tn ; `@ayadi1996`, `@baccouche2008`.
- *Statut* : **à chercher** (corpus JORT 1956-1989 local en PDF, sans couche texte).

---

## 3. Ce qui est déjà trouvé en local

Sauf mention contraire, les chemins sont relatifs à `/home/benjello/projets/PDFs-legislation-tunisie/`.

### 3.1 Faits déjà établis localement (à ne pas re-chercher)

| Fait établi | Preuve locale |
|---|---|
| **Barème LF 2017** : 0→5 000 D : 0 % ; 5 000,001→20 000 : 26 % ; 20 000,001→30 000 : 28 % ; 30 000,001→50 000 : 32 % ; au-delà de 50 000 : 35 % | `PDFs/Lois_de_Finances/Loi_de_Finances_2017.pdf`, art. 14-1 (couche texte OK) |
| **Véhicule et publication du barème 2017** : art. 14-1 de la **loi n° 2016-78 du 17 décembre 2016** (LF pour 2017), modifiant l'art. 44 §I du code IRPP-IS ; mention interne « N° 105 — 27 décembre 2016 » ; application aux revenus réalisés à partir du 1er janvier 2017 | idem + `markdown_output/Code_de_lIRPP_et_IS_2019.md` ligne 813, annotation « (Modifié Art 14-1 LF 2016-78 du 17/12/2016) » |
| **Mesures IRPP connexes de la LF 2017** : plafonnement à 2 000 D d'une déduction de l'art. 26 ; retenue de 20 % sur rétributions provisoires, avec dispense si salaire annuel net ≤ 5 000 D (art. 53 §II du code) ; abrogations liées à la LF 2014 et à la LFC 2015 | `Loi_de_Finances_2017.pdf`, art. 14-2 à 14-6 |
| **Barème LF 2025 (complet)** : art. 36-1, modifiant l'art. 44 §I — 0→5 000 D : 0 % ; 5 000,001→10 000 : 15 % ; 10 000,001→20 000 : 25 % ; 20 000,001→30 000 : 30 % ; 30 000,001→40 000 : 33 % ; 40 000,001→50 000 : 36 % ; 50 000,001→70 000 : 38 % ; **au-delà de 70 000 : 40 %**. Application aux revenus réalisés à partir du 1er janvier 2025 | `PDFs/Lois_de_Finances/Loi_de_Finances_2025.pdf` (couche texte OK) ; strictement concordant avec `openfisca_tunisia/parameters/impot_revenu/bareme.yaml` |
| **Véhicule et publication du barème 2025** : **loi n° 2024-48 du 9 décembre 2024** portant loi de finances pour l'année 2025 ; pied de page du texte officiel : « Journal Officiel de la République Tunisienne — 10 décembre 2024 — N° 149 », p. 3430 (page voisine de l'art. 36) | `Loi_de_Finances_2025.pdf`, page de garde et pieds de page. **Confirme** l'indication portée par openfisca (« JORT n° 149/2024 ») ; le doute né de la troncature du corpus local est levé |
| **Absence de modification de l'art. 44 §I entre 2000 et 2016, vérifiée article par article** : les mentions de l'« article 44 du code » dans les LF de la période portent toutes sur d'**autres paragraphes** — §II (minimum d'impôt) : art. 42 LF 2006, art. 48 LF 2014, art. 10 LFC 2014, art. 16 LF 2019 ; §III (plus-value immobilière) : art. 47 LF 2013 ; §IV (régime forfaitaire) : LF 2010 (contrôle), art. 37 LF 2011 (abrogation et transfert à l'art. 44 bis). La mention de la LF 2015 vise l'article 44 du **code des droits et procédures fiscaux**, sans rapport | balayage `pdftotext` + lecture du contexte de chaque occurrence dans `PDFs/Lois_de_Finances/` |
| **Mécanisme de la CSS des personnes physiques** : l'art. 53 de la LF 2018 la définit comme la différence entre l'impôt calculé sur le barème de l'art. 44 **majoré de un point sur chaque taux de tranche** et l'impôt calculé sur le barème non majoré | `Loi_n_2017-66_du_18_décembre_2017…pdf`, art. 53 |
| **Aucune modification du barème entre 2000 et 2016** : aucune occurrence de la formule-type de modification du barème dans les LF 2000 à 2016 (l'unique occurrence de « barème de l'impôt sur le revenu », en LF 2011, renvoie au texte de l'art. 44 quinquies sur la cession de fonds de commerce). Corroboré par le balayage des mentions de l'art. 44, ligne ci-dessus | balayage `pdftotext` de `PDFs/Lois_de_Finances/*.pdf` |
| **LF 2026 = loi n° 2025-17 du 12 décembre 2025** | `PDFs/Notes_Communes/Note_Commune_N02 Commentaire_des_dispositions_de_larticle_53_de_la_loi_n2025-17_du_12_décembre_2025_portant_loi_de_finances_pour_lannée_2026_relatives.pdf` (note commune n° 2/2026, en arabe ; objet : extension de la facturation électronique aux prestations de services) |
| **Piste LF 2026 / régime estimatif** : l'art. 91 ajoute un paragraphe à l'art. 44 ter du code IRPP-IS (régime estimatif optionnel sous 100 000 D de CA). **Repérage sur couche texte arabe, à confirmer sur texte officiel — cf. Q6** | `PDFs/Lois_de_Finances/Loi_des_Finances_2026_disponible_en_langue_arabe_uniquement.pdf` |

### 3.2 Corpus JORT local

- **`PDFs/JORT/<année>/fr/` et `/ar/`**, années **1956 à 2026**, convention de nommage
  `Jo0NN<année>.pdf` (français) / `Ja0NN<année>.pdf` (arabe). Environ 344 Mo.
- **`PDFs/JORT/1989/fr/Jo08889.pdf`** : dernier numéro de 1989, correspond à l'URL pist.tn déjà
  enregistrée pour `loi-irpp-is-1989`. **Aucune couche texte** (160 caractères extraits) → **OCR
  requis** (outillage présent dans le dépôt : `convert_jort_to_md.py`, `tessdata/`).
- **Lacunes de fin d'année, déterminantes pour cette commande** : le corpus s'arrête à
  **n° 119 de 2024 (1er octobre 2024)**, **n° 120 de 2025 (30 septembre 2025)** et **n° 56 de 2026
  (2 juin 2026)**, dans les deux éditions. **Les JORT de décembre portant la LF 2025 et la LF 2026
  ne sont donc pas locaux** et doivent être récupérés sur pist.tn.
- **Attention à ne pas surinterpréter cette troncature** : elle tient à l'arrêt de la collecte, non
  à la numérotation. Le texte officiel de la LF 2025 porte bien « N° 149 — 10 décembre 2024 », ce
  qui est cohérent avec une trentaine de numéros publiés entre le 1er octobre et le 10 décembre.
  L'indication d'openfisca est donc **confirmée**, pas douteuse.
- **`markdown_output/JORT/<année>/{fr,ar}/`** : conversions déjà réalisées, mais **très partielles**
  (35 années présentes, quelques numéros par année seulement ; qualité OCR inégale — voir
  `markdown_output/JORT/1991/fr/Jo01491.md`). Rien pour 1989 hors `Jo00489`, `Jo01789`, `Jo04189` ;
  un seul numéro pour 1990 (`Jo05590`).

### 3.3 Lois de finances et doctrine administrative

- **`PDFs/Lois_de_Finances/`** (35 fichiers) : LF **2000 à 2026** et lois de finances
  complémentaires (2002, 2004, 2012 à 2016). Couche texte présente sauf pour la LFC/LF 2021, 2022
  et 2023 (`Loi_n_2020-46…2021`, `Décret-loi_n_2021-21…2022`, `Loi_de_Finances_2023`) → OCR requis.
  LF 2026 disponible **en arabe uniquement**.
  **Lacune majeure : aucune LF de 1990 à 1999**, période qui concentre pourtant Q2 et Q3.
- **`PDFs/Notes_Communes/`** (1 223 fichiers) : doctrine administrative DGI. Pièce clé identifiée
  pour Q4 : `Note_Commune_numéro 3  Commentaire_des_dispositions_de_larticle_14_de_la_loi_n_2016-78_du_17_décembre_2016_portant_loi_de_finances_pour_lannée_2017_re.pdf`
  — **sans couche texte, OCR requis** ; devrait reproduire l'ancien et le nouveau barème côte à côte.
- **`PDFs/Code_de_lIRPP_et_IS/`** et **`markdown_output/Code_de_lIRPP_et_IS_<année>.md`**
  (millésimes 2019, 2020, 2021, 2022, 2023, 2025) : **meilleur atout local de la commande**. Ces
  codes consolidés portent l'**historique de modification annoté en ligne**, par exemple
  « (Modifié Art 14-1 LF 2016-78 du 17/12/2016) », « (Ajouté Art.44 LF.93-125 du 27/12/93) »,
  « (Modifié Art. 15 LF 2001-123 du 28/12/2001) ». Ils permettent de **dater chaque modification
  des articles 40, 44, 44 bis à 44 sexies et 53 avec numéro de loi et date**, donc de cibler
  précisément quels JORT aller chercher. **Ils ne donnent en revanche ni le numéro ni la page du
  JORT** : cette étape reste à faire sur pist.tn.
- **`data/iort/textes/md/`** (~32 000 fichiers) et `data/pm_gov/` : arrêtés, décrets, circulaires ;
  peu utile pour le barème, potentiellement utile pour les barèmes agricoles annexes et les
  décrets d'application du régime forfaitaire.

### 3.4 Paramètres openfisca-tunisia — **à traiter comme des indices, pas comme une autorité juridique**

Chemins relatifs à `/home/benjello/projets/openfisca-tunisia/openfisca_tunisia/parameters/`.

> **Avertissement à porter au rédacteur.** Les dates d'effet portées par ces fichiers YAML sont des
> repères d'implémentation, souvent sans référence légale ; elles indiquent **où chercher dans le
> JORT**, elles ne prouvent rien. Deux défauts avérés :
> - `impot_revenu/bareme.yaml` porte `1990-01-01` comme date plancher **sans aucune référence**
>   antérieure à 2017, et son encodage pré-2017 est **manifestement incomplet** : il s'arrête à un
>   seuil de 20 000 D au taux de 30 %, sans tranche supérieure, alors que le précis comme la
>   comparaison LF 2017 supposent l'existence d'un taux marginal de 35 %. **Construire la colonne
>   « 1990 » du tableau d'évolution à partir de ce fichier produirait un tableau faux.**
> - `impot_revenu/deductions/famille/chef_de_famille.yaml` date l'effet au 1er janvier 2019 mais
>   référence l'article 55 de la **loi n° 2017-66 (LF pour 2018)** : incohérence date/véhicule.

| Fichier | Ce qu'il apporte | Ce qu'il ne prouve pas |
|---|---|---|
| `impot_revenu/bareme.yaml` | dates de rupture 1990 / 2017 / 2025 ; barème 2025 complet ; référence 2025 (art. 36 LF 2024-48 du 9 déc. 2024) | encodage pré-2017 incomplet ; date 1990 non référencée ; référence JORT 2024 douteuse |
| `impot_revenu/deductions/famille/*.yaml` | valeurs et dates pour chef de famille, enfants, parent à charge, infirme | références JORT absentes ; incohérence signalée ci-dessus |
| `impot_revenu/exoneration/seuil.yaml` | seuil de 5 000 D daté de 2014 | **aucune référence** — c'est exactement l'objet de Q7 |
| `impot_revenu/minimum_impot/taux.yaml` | 0 % (1990) → 60 % (2014) → 45 % (2020) | aucune référence (Q9) |
| `impot_revenu/tspr/*.yaml` | abattement 10 %, plafond 2 000 D, abattement salaire minimum 500 D (2005) → 1 000 D (2010) | aucune référence (Q11) |
| `impot_revenu/regimes_speciaux/`, `impot_revenu/bic/forf/` | tarifs forfaitaires, retenue libératoire ; commentaires internes signalant des valeurs « à titre d'exemple » | valeurs explicitement non fiabilisées (Q12) |
| `impot_revenu/contribution_budget_etat.yaml` | barème en jours de salaire, 2014 | aucune référence (Q13) |
| `prelevements_sociaux/contribution_sociale_solidarite/salarie.yaml` | **le mieux documenté** : art. 53 LF 2017-66 ; art. 22 décret-loi 2022-79 (LF 2023, baisse temporaire à 0,5 pt pour 2023-2025) ; maintien LF 2025 ; notes communes 1/2018 et 1/2023 | URL de référence pointant vers un dépôt GitLab tiers → **à remplacer par des URL pist.tn** ; rien sur 2026 (Q10) |

### 3.5 Autres pistes locales

- `/home/benjello/projets/ceq-tunisie/` : jeu **CEQ Tunisie 2021** (`CEQ_TUN21_March2025`,
  `TUN_FiscalSim2024_Info.xlsx`), méthodologie d'incidence fiscale par décile. Piste sérieuse pour
  construire une **ventilation par décile documentée** en substitut ou en complément du chiffre INS
  relayé par la presse (Q14) — sous réserve de vérifier ce qui est effectivement calculé (IRPP seul
  vs. incidence totale).
- Dépôt **`tunisia-data`** : point d'entrée pour les séries de recettes fiscales (Q17), avec fiches
  de provenance (`sources/*.md`) et clés de citation `dataset` à créer côté bibliographie.

---

## 4. Structure cible proposée pour la section IRPP

Logique d'entonnoir, avec mention explicite des **sous-secteurs juridiques** (régime réel /
régime forfaitaire BIC / régime estimatif ; catégories de revenus de l'art. 8 du code).

```
## L'impôt sur le revenu des personnes physiques (IRPP)

### Antécédents : de la fiscalité beylicale au système cédulaire
  #### L'héritage beylical et colonial (avant 1956)      [texte actuel, conservé]
  #### Le système cédulaire et l'IGR (1956-1989)          [Q18 — sourcer sur textes]

### L'architecture actuelle : le code de l'IRPP et de l'IS (1989)
  - champ, catégories de revenus, articulation IRPP / IS
  - sous-secteurs : régime réel, régime forfaitaire BIC, régime estimatif optionnel (LF 2026)
  → citer [@loi-irpp-is-1989] (clé déjà disponible, jamais utilisée)

### L'évolution du barème, 1990-2026
  - récit par génération de barème : 1990 → 1991 ? → (stabilité) → 2017 → 2025 → 2026 ?
  - chaque génération adossée à son texte modificatif et à sa référence JORT pist.tn

  [TABLEAU 1] Générations successives du barème de l'IRPP, 1990-2026
    → une colonne par GÉNÉRATION de barème (et non par année) ; lignes : tranches et taux ;
      ligne « en vigueur du … au … » ; ligne « texte modificatif (art., loi, JORT) ».
      Rend visibles les périodes de stabilité sans colonnes redondantes.
    → figdata : `fig_bareme_irpp_generations.csv` (+ `.csv.yml` de provenance)

  [FIGURE 1] Taux marginal supérieur et nombre de tranches, 1990-2026
    → série annuelle en escalier, deux axes ; satisfait la règle « pas de chiffre isolé » pour
      les « 68 % », « 35 % », « 40 % », « 16 / 6 / 5 / 8 tranches » aujourd'hui isolés.
    → figures/bareme_irpp.py ; figdata : `fig_bareme_irpp_taux_marginal.csv`

  [FIGURE 2, ENRICHISSEMENT] Taux moyen d'imposition selon le revenu, par génération de barème
    → superposition de 3-4 courbes (1990, pré-2017, 2017, 2025) ; visualise directement le débat
      sur la progressivité, sans que le précis ait à le trancher.
    → figdata : `fig_bareme_irpp_taux_moyen.csv`

### Les paramètres périphériques du barème
  - déductions pour charges de famille ; abattements sur salaires ; seuil d'exonération ;
    minimum d'impôt ; contribution sociale de solidarité

  [TABLEAU 2] Paramètres périphériques de l'IRPP : valeurs et dates d'effet
    → une ligne par paramètre, une colonne par date de changement, avec le texte modificatif.
      Squelette déjà disponible via openfisca (§3.4), à confirmer intégralement sur JORT.
    → figdata : `fig_irpp_parametres_peripheriques.csv`

### Les régimes d'imposition : réel, forfaitaire, estimatif
  - conditions d'éligibilité, tarifs, mesures de retrait ; réforme LF 2026 (Q6, Q12)

### Rendement et incidence
  [FIGURE 3] Recettes d'IRPP en % du PIB et en % des recettes fiscales, série longue   [Q17]
  [FIGURE 4 ou TABLEAU 3] Taux d'imposition effectif par décile                        [Q14]
    → n'introduire QU'AVEC la ventilation complète par décile et la définition d'assiette ;
      à défaut, laisser un TODO plutôt que de republier le couple 18,2 % / 16,7 %.

### Débats et appréciations
  - positions exposées EN REGARD et attribuées nommément : justification gouvernementale (Q15),
    lecture de @touaiti2026, doctrine fiscale, organisations internationales, partenaires
    sociaux (Q16). Le précis documente les positions, il n'arbitre pas.
```

**Ordre de traitement recommandé** (dépendances) : Q1, Q2, Q4 (les trois colonnes manquantes du
tableau 1) → Q3 et Q6 (bornes de la série) → Q7 à Q10 (tableau 2) → Q14 et Q15 (section
« débats ») → le reste en enrichissement.

---

## 5. Pour l'agent bibliographe

Signalements issus de l'inventaire ; **aucun fichier de bibliographie n'a été modifié** par cette note.

1. **Entrées parasites à nettoyer** — deux pièces jointes Zotero exposées comme des références
   citables : `23975222/K2B3EV4C` (« bastier_1997_fiscalite_coloniale.pdf ») dans
   `precis/fr/fiscalite/references.json`, et `23975222/DKA289MH` (« loi_2019_10_amen_social.pdf »)
   dans `precis/fr/references.json`. Les références réelles correspondantes (`bastier1997`,
   `loi-amen-social-2019`) existent déjà.
2. **`@yaich`** : ni année ni édition, alors que l'ouvrage *Les impôts en Tunisie* est réédité
   annuellement. Pour un usage en appui d'un état du droit daté, préciser le millésime cité.
3. **Clés `legislation` à créer** (une par texte confirmé, avec **URL pist.tn**) : loi de finances
   pour 1991 (à identifier, Q2) ; loi n° 2013-54 du 30 décembre 2013 (LF 2014) ; loi n° 2016-78 du
   17 décembre 2016 (LF 2017) ; loi n° 2017-66 du 18 décembre 2017 (LF 2018) ; décret-loi
   n° 2022-79 du 22 décembre 2022 (LF 2023) ; **loi n° 2024-48 du 9 décembre 2024** (LF 2025 — numéro, date et JORT n° 149 du 10 décembre 2024
   vérifiés sur le texte officiel) ; **loi n° 2025-17 du 12 décembre 2025** (LF 2026 — numéro et
   date corroborés par la note commune n° 2/2026) ; loi n° 2014-54 du 19 août 2014 (LFC 2014) ;
   loi n° 2023-13 du 11 décembre 2023 (LF 2024, corroborée par une note commune).
   Les numéros de LF antérieurs (93-125, 96-113, 98-111, 99-101, 2001-123, 2004-90, 2005-106,
   2006-85, 2007-70, 2009-71) apparaissent dans les annotations du code consolidé et sont
   utilisables comme **pistes**, mais chacun doit être confirmé sur le JORT avant citation.
4. **Doctrine administrative** : prévoir un type de référence pour les **notes communes** de la DGI
   (au minimum NC 3/2017, NC 1/2018, NC 1/2023, NC 2/2026), très utilisées pour l'interprétation.
5. **Sources de données** : clés `dataset` à créer pour les séries de recettes fiscales (Q17) et
   pour la publication INS d'incidence (Q14), en cohérence avec `docs/notes/biblio-a-rapatrier.md`.
6. **Rappel** : toute clé ajoutée à la main dans un `references.json` doit être remontée dans
   Zotero (groupe 6529669) pour être stable, `scripts/sync_biblio.py` faisant autorité en sens
   Zotero → `references.json`.
