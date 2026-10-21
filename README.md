# 📜 DOCUMENTATION STRATÉGIQUE & ARCHITECTURE TECHNIQUE
## Projet : Safidy Decision Engine (`safidy-decision-engine`)
**Association Safidy Ifanomezantsoa**

---

### 1. Vision & Concept Général

La plateforme **Safidy Decision Engine** est la centrale de transformation décisionnelle et l'outil de plaidoyer stratégique de l'association *Safidy Ifanomezantsoa*. Elle agit comme une **machine à transformer des données brutes, des doléances et des résolutions en actions priorisées, budgétisées et mesurables**.

Pour préserver nos ressources d'infrastructure tout en assurant une étanchéité parfaite, la plateforme combine deux outils opérationnels distincts au sein du même projet Supabase :

1. **🏛️ SAFIDY Decision Engine (Module Concertations, Colloques & Ateliers) :**
   * Proposé et déployé lors des rencontres, ateliers, colloques ou réunions de concertation.
   * Traite l'ingestion multi-documents (rapports PDF, comptes-rendus Word, tableurs Excel, scans de résolutions) et recense la représentation des **parties prenantes** (partis politiques, société civile, syndicats, groupements de jeunes).

2. **📢 SAFIDY Audit Citoyen (Module de Signalement & Anti-Corruption) :**
   * Exploité en continu ou sur des périodes ciblées (campagnes de sensibilisation et de lutte contre la corruption).
   * Permet aux citoyens de saisir leurs constats, retards et surcoûts administratifs.
   * **Reçu d'Audit Instantané :** Dès la validation, le citoyen obtient un récapitulatif/récépissé officiel de sa déposition sur son écran.
   * **Passerelle Moteur :** L'ensemble des données d'audit collectées sur une période donnée alimente directement *Safidy Decision Engine*.

---

### 2. Temporalité, Campagnes & Fenêtres Décisionnelles

Afin d'offrir une traçabilité totale aux partenaires et bailleurs de fonds (ex: FID, AfricTivistes, Code for Africa), le moteur décisionnel opère selon deux modes temporels :

* **Mode Collecte Continue (Temps Réel) :** Ingestion au fil de l'eau des dénonciations d'audit et des documents d'ateliers.
* **Mode Fenêtre Décisionnelle (Revue & Campagnes) :** Clôture ou ciblage d'une période d'analyse (ex: *Campagne T1* ou *Post-Atelier Régional*). C'est lors de ces fenêtres que la machine exécute le croisement des Faiblesses (Audits) et Opportunités (Ateliers) pour générer la feuille de route stratégique.

---

### 3. Matrice de Priorisation & Outils Budgétaires Bailleurs

Après traitement des rapports et preuves reçus, *Safidy Decision Engine* dégage automatiquement des propositions d'actions classées selon leur niveau d'urgence et leur impact :

#### A. Ordre de Priorité des Actions :
* 🔴 **URGENT & IMPORTANT (Court Terme — 0 à 3 mois) :** Mesures d'urgence ciblées sur les services publics présentant un taux élevé de pression de corruption ou un lourd préjudice financier pour les citoyens.
* 🟠 **IMPORTANT (Moyen Terme — 3 à 6 mois) :** Réformes administratives structurantes fondées sur les consensus issus des ateliers et concertations.
* 🟢 **À FAIRE PLUS TARD (Long Terme — 6 à 12 mois) :** Orientations stratégiques et réformes de fond nécessitant un cadre législatif étendu.

#### B. Modèle de Simulation Budgétaire & Impact Financier :
* **Manque à gagner & Préjudice :** Calcul automatisé des surcoûts subis par les usagers et des manques à gagner pour les recettes publiques.
* **Graphe de Simulation d'Impact :** Projection chiffrée de l'impact des réformes (ex: *estimation de hausse des recettes administratives de +10% à +20% suite au déploiement d'un suivi citoyen*).
* **Budget de Plaidoyer :** Chiffrage des enveloppes financières requises pour mener les actions de suivi et de plaidoyer auprès des autorités.

---

### 4. Architecture des 4 Volets du Dashboard Analytique (`dashboard.html`)

Le tableau de bord centralise et visualise ces données à travers 4 espaces étanches :

1. **📢 Volet 1 — Audit Citoyen & Anti-Corruption :** Graphiques et KPI sur les délais, le taux de corruption et les pertes financières en Ariary.
2. **🏛️ Volet 2 — Concertations & Ateliers :** Suivi du volume de résolutions, classement par thématiques et analyse de la représentation des parties prenantes cross-colloques.
3. **📁 Volet 3 — Coffre-fort des Preuves (Supabase Storage) :** Répertoire sécurisé permettant la consultation et le téléchargement des pièces justificatives (scans, factures, PDF, DOCX, XLSX).
4. **🎯 Volet 4 — Vue Consolidée SWOT/TOWS & Fiches SMART :** Matrice de priorisation, simulation budgétaire et générateur de **Fiches d'Action SMART** imprimables pour le travail officiel de plaidoyer.

---

### 5. Sécurité, Anonymat & Gouvernance
* **Importation Directe :** Module d'upload direct de fichiers réels (fin des liens externes complexes).
* **Anonymat Garanti :** Les données restituées dans les graphiques et rapports décisionnels sont entièrement agrégées et anonymisées.
* **Propriété Exclusive :** La plateforme est la propriété exclusive de l'association **Safidy Ifanomezantsoa**.
