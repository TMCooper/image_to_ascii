import glob
import os

# Votre chemin de base où rechercher les images
PATH = r"C:\Users\pokem\OneDrive\Bureau\Code\image_to_ascii"

# Liste des extensions d'image à inclure
image_extensions = ['*.jpg', '*.jpeg', '*.png']

# Liste pour stocker tous les chemins de fichiers image trouvés
images_path = []

for extension in image_extensions:
    # Créer le motif complet pour glob
    pattern = os.path.join(PATH, extension)
    # Récupérer tous les fichiers correspondant au motif et les ajouter à images_path
    images_found = glob.glob(pattern)
    images_path.extend(images_found)

print(f'{images_path}\n')
