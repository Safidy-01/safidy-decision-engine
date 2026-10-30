import os
import re
import io
from supabase import create_client
from pypdf import PdfReader

# --- CONFIGURATION SUPABASE ---
SUPABASE_URL = "https://tunanbanizxowofzkjllv.supabase.co"
SUPABASE_KEY = "sb_publishable_OyEsfDZaWZv..." # Ta clé anon

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
BUCKET_NAME = "documents_preuves"

def sauvegarder_analyse_swot(nom_fichier, actions_urgentes, actions_importantes, forces, faiblesses):
    """ Enregistre les résultats dans la table analyses_swot """
    data = {
        "nom_fichier": nom_fichier,
        "actions_urgentes": str(actions_urgentes),
        "actions_importantes": str(actions_importantes),
        "forces": str(forces),
        "faiblesses": str(faiblesses)
    }
    try:
        response = supabase.table("analyses_swot").insert(data).execute()
        print(f"✅ Enregistré dans Supabase pour : {nom_fichier}")
        return response
    except Exception as e:
        print(f"❌ Erreur sauvegarde Supabase : {e}")
        return None

def recuperer_et_analyser_documents():
    print("📂 Connexion au bucket Supabase...")
    try:
        files = supabase.storage.from_(BUCKET_NAME).list()
        for file in files:
            nom_fichier = file['name']
            if nom_fichier.startswith('.'):
                continue
            
            print(f"📄 Analyse de : {nom_fichier}")
            res = supabase.storage.from_(BUCKET_NAME).download(nom_fichier)
            pdf_file = io.BytesIO(res)
            reader = PdfReader(pdf_file)
            texte = ""
            for page in reader.pages:
                texte += page.extract_text() or ""
            
            # Détection rapide de mots-clés
            forces = re.findall(r'.*force.*', texte, re.IGNORECASE)
            faiblesses = re.findall(r'.*faiblesse.*', texte, re.IGNORECASE)
            urgentes = re.findall(r'.*urgent.*', texte, re.IGNORECASE)
            importantes = re.findall(r'.*important.*', texte, re.IGNORECASE)
            
            # Sauvegarde automatique dans la table Supabase
            sauvegarder_analyse_swot(
                nom_fichier=nom_fichier,
                actions_urgentes="\n".join(urgentes),
                actions_importantes="\n".join(importantes),
                forces="\n".join(forces),
                faiblesses="\n".join(faiblesses)
            )
            
    except Exception as e:
        print(f"❌ Erreur lors du traitement : {e}")

if __name__ == "__main__":
    recuperer_et_analyser_documents()
