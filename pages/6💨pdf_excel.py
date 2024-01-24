import streamlit as st
from func import pdf_to_excel


st.set_page_config(page_title="PDF == > Excel", page_icon="💨")
st.write("Convertir un PDF en Excel")

file = st.file_uploader(label="Importer un fichier PDF", type=["pdf"])

if file:
    excel_file = pdf_to_excel(file)
    st.download_button(label="Télécharger le fichier", file_name=f"{file.name}.xlsx", data=excel_file)
    