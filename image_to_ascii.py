from ascii_magic import AsciiArt
from PIL import ImageEnhance
import glob
import os

EXTENTION = ".html"
NAME_AD = "_ascii"
IMAGES_EXTENTIONS = ['*.jpg', '*.jpeg', '*.png']

def main():
    choix = input("Voulez vous votre images en noir et blanc ou couleur ? (NB/C) : ").lower()
    print("si vous marquer N c'est le dossier ou le programme est situer que les images vont être enregistré\n si vous avez une images en particullier vous pouvez aussi la mettre dirrectement")
    PATH_C = input("quelle est votre sources ? : ")

    while choix not in ["nb", "c"]:
            choix = input("Veulliez saisir C/NB : ").lower()

    if PATH_C not in ["N", "n"]:
        PATH_IMAGES_C = os.path.join(PATH_C, "Ascii_Images")

        if choix in ["nb"]:
            
            choix = input("Voulez vous save la/les image(s) ? Y/N : ").lower()

            while choix not in["y", "n"]:
                choix = input("Veulliez saisir Y ou N : ").lower()

            images_path = glob.glob(os.path.join(PATH_C,'*.*'))
            if not images_path:
                    print("Aucun fichier trouvé dans le dossier sources.")
            else:
                print("Fichiers trouvés :")
                for PATH_C in images_path:
                    # Extraire le nom du fichier
                    file_name = os.path.basename(PATH_C)
                    print(file_name)
                    file_just_name, file_ext  = os.path.splitext(file_name)

                    ascii = AsciiArt.from_image(f'{PATH_C}')
                    ascii.image = ImageEnhance.Brightness(ascii.image).enhance(0.2)
                    ascii.to_terminal()

                    if choix in ["Y", "y"]:
                        if not os.path.exists(PATH_IMAGES_C):
                            os.mkdir(PATH_IMAGES_C)

                        images = os.path.join(PATH_IMAGES_C, file_just_name + NAME_AD + EXTENTION)
                        ascii.to_html_file(images, columns=200, width_ratio=2)
                        print("Enregistrement effectuer !")
            
            if choix in ["n", "y"]:
                print("Tache termine !")
        
        if choix in ["c"]:
            PATH_IMAGES_C = os.path.join(PATH_C, "Ascii_Images")

            choix = input("Voulez vous save la/les image(s) ? Y/N : ").lower()

            while choix not in["y", "n"]:
                choix = input("Veulliez saisir Y ou N : ").lower()
            
            images_path = glob.glob(os.path.join(PATH_C,'*.*'))

            if not images_path:
                print("Aucun Fichier trouvé dans le dossier sources.")

            else:
                print("Fichier Troués :")
                for PATH_C in images_path:
                    file_name = os.path.basename(PATH_C)
                    print(file_name)
                    file_just_name, file_ext = os.path.splitext(file_name)

                    ascii = AsciiArt.from_image(f'{PATH_C}')
                    ascii.to_terminal()

                    if choix in ["Y", "y"]:
                        if not os.path.exists(PATH_IMAGES_C):
                            os.mkdir(PATH_IMAGES_C)

                        images = os.path.join(PATH_IMAGES_C, file_just_name + NAME_AD + EXTENTION)
                        ascii.to_html_file(images, columns=200, width_ratio=2)
                        print("Enregistrement effectuer !")
            
            if choix in ["n", "y"]:
                print("Tache termine !")

    if PATH_C in ["N", "n"]:
        PATH = os.path.dirname(os.path.abspath(__file__))
        PATH_IMAGES =  os.path.join(PATH, "Ascii_Images")
        images_path = []
        
        if choix in ["c"]:
            choix = input("Voulez vous save la/les image(s) ? Y/N : ").lower()

            while choix not in["y", "n"]:
                choix = input("Veulliez saisir Y ou N : ").lower()

            for extension in IMAGES_EXTENTIONS:

                pattern = os.path.join(PATH, extension)
                images_found = glob.glob(pattern)
                images_path.extend(images_found)
            
            if not images_path:
                print("Aucun fichier image trouvé dans le dossier spécifié.")

            else:
                for PATH in images_path:
                    file_name = os.path.basename(PATH)  # Nom du fichier avec extension
                    file_just_name, file_ext = os.path.splitext(file_name)
                    
                    print(f'Fichier Trouvé : {file_name}')
                    ascii = AsciiArt.from_image(f'{PATH}')
                    ascii.to_terminal()

                    if choix in ["y"]:
                        if not os.path.exists(PATH_IMAGES):
                            os.mkdir(PATH_IMAGES)
                        
                        images = os.path.join(PATH_IMAGES, file_just_name + NAME_AD + EXTENTION)
                        ascii.to_html_file(images, columns=200, width_ratio=2)
                        print("Eregistrement effectuer !")

            if choix in ["N", "n"]:
                print("Tache termine !")
        
        if choix in ["NB", "nb"]:
            choix = input("Voulez vous save la/les image(s) ? Y/N : ").lower()

            while choix not in["y", "n"]:
                choix = input("Veulliez saisir Y ou N : ").lower()

            for extension in IMAGES_EXTENTIONS:

                pattern = os.path.join(PATH, extension)
                images_found = glob.glob(pattern)
                images_path.extend(images_found)
            
            if not images_path:
                print("Aucun fichier image trouvé dans le dossier spécifié.")

            else:
                for PATH in images_path:
                    file_name = os.path.basename(PATH)  # Nom du fichier avec extension
                    file_just_name, file_ext = os.path.splitext(file_name)
                    
                    print(f'Fichier Trouvé : {file_name}')
                    ascii = AsciiArt.from_image(f'{PATH}')
                    ascii.image = ImageEnhance.Brightness(ascii.image).enhance(0.2)
                    ascii.to_terminal()

                    if choix in ["Y", "y"]:
                        if not os.path.exists(PATH_IMAGES):
                            os.mkdir(PATH_IMAGES)
                        
                        ascii.image = ImageEnhance.Brightness(ascii.image).enhance(0.2)
                        images = os.path.join(PATH_IMAGES, file_just_name + NAME_AD + EXTENTION)
                        ascii.to_html_file(images, columns=200, width_ratio=2)
                        print("Eregistrement effectuer !")
        
            if choix in ["n"]:
                print("Tache termine !")

if __name__ == "__main__":
    main()
