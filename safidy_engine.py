import os
import re
from supabase import create_client
from pypdf import PdfReader
import io

# --- CONFIGURATION SUPABASE ---
# Utilisation de tes identifiants (la clé anon est sécurisée par tes règles RLS)
SUPABASE_URL = "https://tunanbanizxowofzkjql.supabase.co"
SUPABASE_KEY = "sb_publishable_OyEsfDZaWZwhe0pkPkqtWQ_TPtbQ5iR"  # Remplace par ta vraie clé anon

# Initialisation du client Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
BUCKET_NAME = "documents_preuves"

def recuperer_et_analyser_documents():
    print("📂 Connexion au bucket Supabase 'documents_preuves'...")
    try:
        # Liste les fichiers présents dans le bucket
        files = supabase.storage.from_(BUCKET_NAME).list()
        
        if not files:
            print("ℹ️ Aucun fichier trouvé dans le bucket documents_preuves.")
            return

        for file in files:
            file_name = file['name']
            print(f"\n📥 Traitement du document : {file_name}")
            
            # Téléchargement du PDF depuis Supabase Storage
            res = supabase.storage.from_(BUCKET_NAME).download(file_name)
            
            if file_name.lower().endswith('.pdf'):
                # Lecture du PDF
                reader = PdfReader(io.BytesIO(res))
                texte_integral = ""
                for page_num, page in enumerate(reader.pages):
                    texte_integral += page.extract_text() or ""
                
                print(f"✅ Document lu avec succès ({len(reader.pages)} pages). Analyse en cours...")
                
                # Analyse des résolutions et du SWOT
                analyser_contenu_rapport(texte_integral, file_name)
            else:
                print(f"⚠️ Le fichier {file_name} n'est pas un PDF pris en charge.")
                
    except Exception as e:
        print(f"❌ Erreur lors de la connexion ou du traitement : {e}")

def analyser_contenu_rapport(texte, nom_fichier):
    lignes = texte.split('\n')
    
    actions_urgentes = []
    actions_importantes = []
    actions_plus_tard = []
    
    # Mots-clés de ciblage
    mots_urgents = ['urgent', 'immédiat', 'critique', 'maintenant', 'rapidement']
    mots_importants = ['essentiel', 'important', 'stratégique', 'priorité', 'nécessaire']
    
    # Analyse SWOT simplifiée détectée dans le texte
    swot_forces = []
    swot_faiblesses = []
    swot_opportunites = []
    swot_menaces = []

    for ligne in lignes:
        L = ligne.strip()
        if len(L) > 15:
            l_lower = L.lower()
            
            # Détection SWOT basique
            if 'force' in l_lower: swot_forces.append(L)
            elif 'faiblesse' in l_lower: swot_faiblesses.append(L)
            elif 'opportunité' in l_lower: swot_opportunites.append(L)
            elif 'menace' in l_lower: swot_menaces.append(L)
            
            # Tri par matrice de priorité
            if any(mot in l_lower for mot in mots_urgents):
                actions_urgentes.append(L)
            elif any(mot in l_lower for mot in mots_importants):
                actions_importantes.append(L)
            else:
                actions_plus_tard.append(L)

    # Affichage des résultats structurés
    print(f"\n--- RÉSULTATS DE L'ANALYSE POUR : {nom_fichier} ---")
    print(f"🚨 URGENT ({len(actions_urgentes)} actions détectées)")
    print(f"⭐ IMPORTANT ({len(actions_importantes)} actions détectées)")
    print(f"⏳ À FAIRE PLUS TARD ({len(actions_plus_tard)} actions détectées)")
    print(f"📊 Éléments SWOT extraits : {len(swot_forces)} forces, {len(swot_faiblesses)} faiblesses, {len(swot_opportunites)} opportunités, {len(swot_menaces)} menaces.")

if __name__ == "__main__":
    print("🚀 Démarrage du Safidy Engine...")
    recuperer_et_analyser_documents()
