import streamlit as st
from func import TextAreaExtractor


st.set_page_config(page_title="", page_icon="✔")
st.write("Extraction des articles commandés depuis l'email")

data = st.text_area("Contenu du mail")

if data:
    extractor = TextAreaExtractor(data)
    clean_data = extractor.save_in_workbook()

    with open("commande.xlsx", "rb") as file:
        st.download_button("Télécharger le fichier Excel", data=file, file_name="commande.xlsx")
