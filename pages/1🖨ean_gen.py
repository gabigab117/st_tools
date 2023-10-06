import streamlit as st
# https://python-barcode.readthedocs.io/en/stable/
# 3301070000059
from barcode.writer import ImageWriter
from barcode import get_barcode_class
from PIL import Image
import os


st.set_page_config(page_title="EAN generator", page_icon="🖨")
st.write("Générateur d'EANs")

# Choix type EAN (pour le moment 13)
EAN = get_barcode_class('ean13')

eans = st.text_input("Entrez votre EAN13", help="Séparée par une virgule sans espace")
name = st.text_input("Entrer un nom pour vos images")

if eans and name:
    images_list = []
    # Récupérer les eans dans une liste
    eans = eans.split(",")
    
    for i, ean in enumerate(eans):
        # Sauvegarder les eans en images
        my_ean = EAN(ean, writer=ImageWriter())
        fullname = my_ean.save(f'{name}{i}')
        # Ajouter les images dans une liste
        images_list.append(fullname)

    # Ouvrir les images avec PIL
    images = [Image.open(image) for image in images_list]

    # La somme de la hauteur des images et la largeur max
    max_width = max(image.width for image in images)
    max_height = sum(image.height for image in images)

    # Création d'une nouvelles image pour accueil toutes les images crées
    all_eans = Image.new('RGB', (max_width, max_height))
    # Valeur sur l'axe qui prendra à chaque itération la hauteur de l'image en cours
    y = 0

    for image in images:
        all_eans.paste(image, (0, y))
        # Suppression des images
        image_path = os.path.join(os.getcwd(), image.filename)
        os.remove(image_path)
        y += image.height

    # Save de la liste des eans
    all_eans.save(f"eans-{name}.png")
    st.image(all_eans)