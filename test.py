import glob
import os

# Chemin vers le dossier 'sources'
sources_path = r"C:/Users/pokem/OneDrive/Bureau/Code/image_to_ascii/sources"

# Récupérer tous les fichiers dans le dossier 'sources'
image_files = glob.glob(os.path.join(sources_path, '*.*'))  # *.* pour tous les fichiers

if not image_files:
    print("Aucun fichier trouvé dans le dossier sources.")
else:
    print("Noms de fichiers sans extension :")
    for full_path in image_files:
        # Extraire le nom du fichier avec extension
        file_name_with_ext = os.path.basename(full_path)
        
        # Séparer le nom et l'extension
        file_name, file_ext = os.path.splitext(file_name_with_ext)
        
        print(f"- {file_name}")
