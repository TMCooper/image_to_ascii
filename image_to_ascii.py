from ascii_magic import AsciiArt
from PIL import ImageEnhance
import glob
import os

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_IMAGES =  os.path.join(PATH, "Ascii_Images")

EXTENTION = ".html"
NAME_AD = "_ascii"

def main():
    choix = input("Voulez vous votre images en noir et blanc ou couleur ? (NB/C) : ")
    print("si vous marquer N c'est le dossier ou le programme est situer que les images vont être enregistré\n si vous avez une images en particullier vous pouvez aussi la mettre dirrectement")
    PATH_C = input("quelle est votre sources ? : ")

    while choix not in ["NB", "nb", "C", "c"]:
            choix = input("Veulliez saisir C/NB : ")

    if PATH_C not in ["N", "n"]:
        PATH_IMAGES_C = os.path.join(PATH_C, "Ascii_Images")

        if choix in ["NB", "nb"]:
            
            choix = input("Voulez vous save la/les image(s) ? Y/N : ")

            while choix not in["Y", "y", "N", "n"]:
                choix = input("Veulliez saisir Y ou N : ")

            images_path = glob.glob(os.path.join(PATH_C,'*.*'))
            # print(f'images : {images_path}')

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
                        print("Tache Termine !")
            
            if choix in ["N", "n"]:
                print("Tache termine !")
        
        if choix in ["C", "c"]:
            ascii = AsciiArt.from_image(f'{PATH_C}/Rias_Gremory.jpg')
            ascii.to_terminal()
            choix = input("Voulez vous save l'images ? Y/N : ")

            while choix not in["Y", "y", "N", "n"]:
                choix = input("Veulliez saisir Y ou N : ")

            if choix in ["Y", "y"]:
                name_images = input("Quel est le nom de votre images ? : ")

                if not os.path.exists(PATH_IMAGES_C):
                    os.mkdir(PATH_IMAGES_C)

                images = os.path.join(PATH_IMAGES, name_images + EXTENTION)
                ascii.to_html_file(images, columns=200, width_ratio=2)
                print("Tache Termine !")
            
            if choix in ["N", "n"]:
                print("Tache termine !")
    
    if PATH_C in ["N", "n"]:
        if choix in ["C", "c"]:
            print(PATH)
            ascii = AsciiArt.from_image(f'{PATH}/Rias_Gremory.jpg')
            ascii.to_terminal()
            choix = input("Voulez vous save l'images ? Y/N : ")

            while choix not in["Y", "y", "N", "n"]:
                choix = input("Veulliez saisir Y ou N : ")

            if choix in ["Y", "y"]:
                name_images = input("Quel est le nom de votre images ? : ")

                if not os.path.exists(PATH_IMAGES):
                    os.mkdir(PATH_IMAGES)

                images = os.path.join(PATH_IMAGES, name_images + EXTENTION)
                ascii.to_html_file(images, columns=200, width_ratio=2)
                # {os.path.join(PATH_IMAGES,'%(name_images)s.%(ext)s')}
                print("Tache Termine !")
            
            if choix in ["N", "n"]:
                print("Tache termine !")

        if choix in ["NB", "nb"]:
            ascii = AsciiArt.from_image(f'{PATH}/Rias_Gremory.jpg')
            ascii.image = ImageEnhance.Brightness(ascii.image).enhance(0.2)
            ascii.to_terminal()
            choix = input("Voulez vous save l'images ? Y/N : ")
            
            while choix not in["Y", "y", "N", "n"]:
                choix = input("Veulliez saisir Y ou N : ")
            
            if choix in ["Y", "y"]:
                name_images = input("Quel est le nom de votre images ? : ")

                if not os.path.exists(PATH_IMAGES):
                    os.mkdir(PATH_IMAGES)

                ascii.image = ImageEnhance.Brightness(ascii.image).enhance(0.2)
                images = os.path.join(PATH_IMAGES, name_images + EXTENTION)
                ascii.to_html_file(images, columns=200, width_ratio=2)
                print("Tache Termine !")
        
            if choix in ["N", "n"]:
                print("Tache termine !")

if __name__ == "__main__":
    main()
