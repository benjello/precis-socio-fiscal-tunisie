import os
import sys
from google import genai
from google.genai import types

def main():
    if len(sys.argv) < 2:
        print("Aucun fichier à traiter.")
        sys.exit(0)

    files_to_process = sys.argv[1:]
    
    # Initialisation du client Gemini (utilise automatiquement GEMINI_API_KEY)
    try:
        client = genai.Client()
    except Exception as e:
        print(f"Erreur d'initialisation de l'API Gemini : {e}")
        sys.exit(1)
    
    # Lecture du glossaire et des directives
    guidelines_path = "translation_guidelines.md"
    try:
        with open(guidelines_path, "r", encoding="utf-8") as f:
            guidelines = f.read()
    except Exception as e:
        print(f"Attention : Impossible de lire {guidelines_path}. Erreur: {e}")
        guidelines = "Tu es un traducteur professionnel juridique."

    for file_path in files_to_process:
        if not file_path.endswith(".qmd") and not file_path.endswith("_quarto.yml"):
            continue
            
        if not os.path.exists(file_path):
            continue

        if "precis/fr/" in file_path:
            source_lang = "Français"
            target_lang = "Arabe"
            target_path = file_path.replace("precis/fr/", "precis/ar/")
        elif "precis/ar/" in file_path:
            source_lang = "Arabe"
            target_lang = "Français"
            target_path = file_path.replace("precis/ar/", "precis/fr/")
        else:
            continue
            
        print(f"Traduction en cours : {file_path} -> {target_path} ({source_lang} vers {target_lang})")
        
        with open(file_path, "r", encoding="utf-8") as f:
            source_text = f.read()
            
        prompt = f"""
Voici le fichier source en {source_lang} à traduire en {target_lang}.
S'il te plaît, traduis-le entièrement et renvoie UNIQUEMENT le code source traduit, sans aucun commentaire ou explication avant ou après.
Préserve TOUTES les balises Markdown, les blocs de code, l'en-tête YAML (qui commence et finit par ---) et la structure exacte.

Fichier à traduire :
```markdown
{source_text}
```
"""

        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=guidelines,
                    temperature=0.1, # Température basse pour une traduction fidèle et constante
                ),
            )
            
            translated_text = response.text
            
            # Nettoyage des éventuelles balises Markdown rajoutées par l'IA autour de la réponse
            if translated_text.startswith("```markdown\n"):
                translated_text = translated_text[12:]
            if translated_text.endswith("\n```\n"):
                translated_text = translated_text[:-5]
            elif translated_text.endswith("\n```"):
                translated_text = translated_text[:-4]
                
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(translated_text)
            print(f"Succès : {target_path} a été mis à jour.")
            
        except Exception as e:
            print(f"Erreur lors de la traduction de {file_path}: {e}")

if __name__ == "__main__":
    main()
