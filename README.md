# 🏛️ Safidy Decision Engine

**Moteur d'ingestion de concertations citoyennes, d'analyse SWOT/TOWS automatisée et de génération de fiches d'action SMART.**

---

## 🎯 Vision du Projet
Les propositions citoyennes et les synthèses de concertations issues des associations et organisations de la société civile existent déjà mais restent souvent dispersées. **Safidy Decision Engine** agit comme un centre de traitement stratégique (*Digital Processing Center*) :

1. **Ingestion :** Importation des rapports et synthèses de concertation (PDF, Word, Excel).
2. **Traitement IA :** Extraction automatique de la matrice SWOT, croisement stratégique TOWS.
3. **Plan d'Action SMART :** Génération de fiches d'action hiérarchisées (**P0** Urgent, **P1** Important, **P2** Ultérieur).
4. **Régulation & Suivi :** Baromètre d'impact neutre destiné aux bailleurs de fonds et partenaires institutionnels avec indicateurs de conditionnalité et gouvernance claire (Organes responsables et de suivi).

---

## 🛠️ Architecture Technique (Stack 100% Free Tier)

* **Base de Données & Authentification :** [Supabase](https://supabase.com) (PostgreSQL)
* **Moteur IA :** Google Gemini API / OpenAI API
* **Hébergement & Déploiement :** Vercel
* **Gestion du Code :** GitHub

---

## 📊 Structure des Fiches d'Action
Chaque action générée par le moteur comporte :
* **Priorisation :** P0 / P1 / P2
* **Matrice SMART :** Spécifique, Mesurable, Atteignable, Réaliste, Temporel
* **Ventilation Budgétaire :** Calcul paramétrique et décomposition transparente
* **Gouvernance :** Organe responsable & Organe de suivi
* **Régulation Bailleurs :** Conditionnalité de déblocage des fonds
