from ascii_magic import AsciiArt, Back
from PIL import ImageEnhance
import os

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_IMAGES =  os.path.join(PATH, "Ascii_Images")
EXTENTION = ".html"

def main():
    choix = input("Voulez vous votre images en noir et blanc ou couleur ? (NB/C) : ")

    while choix not in ["NB", "nb", "C", "c"]:
        choix = input("Veulliez saisir C/NB : ")

    if choix in ["NB", "nb"]:
        ascii = AsciiArt.from_image('sources/Rias_Gremory.jpg')
        ascii.image = ImageEnhance.Brightness(ascii.image).enhance(0.2)
        ascii.to_terminal()
        choix = input("Voulez vous save l'images ? Y/N : ")
        
        while choix not in["Y", "y", "N", "n"]:
            choix = input("Veulliez saisir Y ou N : ")
        
        if choix in ["Y", "y"]:
            name_images = input("Quel est le nom de votre images ? : ")

            if not os.path.exists(PATH_IMAGES):
                os.mkdir(PATH_IMAGES)

            ascii = AsciiArt.from_image('sources/Rias_Gremory.jpg')
            ascii.image = ImageEnhance.Brightness(ascii.image).enhance(0.2)
            images = os.path.join(PATH_IMAGES, name_images + EXTENTION)
            ascii.to_html_file(images, columns=200, width_ratio=2)
            print("Tache Termine !")
        
        if choix in ["N", "n"]:
            print("Tache termine !")
    
    if choix in ["C", "c"]:
        ascii = AsciiArt.from_image('sources/Rias_Gremory.jpg')
        ascii.to_terminal()
        choix = input("Voulez vous save l'images ? Y/N : ")

        while choix not in["Y", "y", "N", "n"]:
            choix = input("Veulliez saisir Y ou N : ")

        if choix in ["Y", "y"]:
            name_images = input("Quel est le nom de votre images ? : ")

            if not os.path.exists(PATH_IMAGES):
                os.mkdir(PATH_IMAGES)

            ascii = AsciiArt.from_image('sources/Rias_Gremory.jpg')
            images = os.path.join(PATH_IMAGES, name_images + EXTENTION)
            ascii.to_html_file(images, columns=200, width_ratio=2)
            # {os.path.join(PATH_IMAGES,'%(name_images)s.%(ext)s')}
            print("Tache Termine !")
        
        if choix in ["N", "n"]:
            print("Tache termine !")

if __name__ == "__main__":
    main()
