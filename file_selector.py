import os
from aider_vox import models
from pathlib import Path
from aider_vox.utils import is_ignored_file
from litellm import completion

def select_relevant_files(all_files, max_files=10):
    """
    Utilise un modèle LLM pour sélectionner les fichiers les plus pertinents,
    en excluant les fichiers correspondant à .gitignore et .aiderignore.
    """
    model_name = "claude-3-haiku-20240307"  # Utiliser un modèle plus léger pour la sélection
    
    # Filtrer les fichiers ignorés
    filtered_files = [file for file in all_files if not is_ignored_file(file)]
    
    prompt = f"""Voici une liste de fichiers dans un projet. Sélectionnez les {max_files} fichiers les plus importants et pertinents pour le développement du projet, en vous concentrant sur les fichiers principaux, les concepts clés et les discussions importantes. Ignorez les fichiers de configuration, les fichiers temporaires et les fichiers moins importants. Répondez uniquement avec la liste des noms de fichiers sélectionnés, un par ligne.

Liste des fichiers :
{', '.join(filtered_files)}
"""
    
    response = completion(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    selected_files = response.choices[0].message.content.strip().split('\n')
    
    return [file.strip() for file in selected_files if file.strip() in filtered_files][:max_files]  # Limit to max_files
