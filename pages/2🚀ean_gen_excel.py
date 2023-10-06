import streamlit as st
import pandas as pd
from barcode.writer import ImageWriter
from barcode import get_barcode_class
from PIL import Image
import os

st.set_page_config(page_title="Génération d'EANS depuis Excel", page_icon="🚀")

file = st.file_uploader("Importer le fichier excel", help="Les EANs doivent être en colonne A")
if file:
    eans = []
    df = pd.read_excel(file, names=['A', 'B'], header=None)
    
    for el in df['A']:

        if len(str(el)) == 13:
            eans.append(str(el))

# Choix type EAN (pour le moment 13)
EAN = get_barcode_class('ean13')

name = st.text_input("Entrer un nom pour vos images")

if file and name:
    images_list = []
    
    for i, ean in enumerate(eans):
        # Sauvegarder les eans en images
        my_ean = EAN(ean, writer=ImageWriter())
        fullname = my_ean.save(f'{name}{i}')
        # Ajouter les images dans une liste
        images_list.append(fullname)

    # Ouvrir les images avec PIL et les redimensionner
    images = []
    for i, image in enumerate(images_list):
        resized_image = Image.open(image)
        resized_image.thumbnail((200, 200))
        resized_image.save(f"{name}{i}.png")
        images.append(resized_image)
    # images = [Image.open(image) for image in images_list] ancienne compréhension de liste

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