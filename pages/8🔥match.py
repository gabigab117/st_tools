import streamlit as st
from func import Matchinator

st.set_page_config(page_title="Rejets + cadencier", page_icon="🔥")


rejects = st.file_uploader("Rejets", type=["xlsx"])
orderable = st.file_uploader("Cadencier", type=["xlsx"])

if rejects and orderable:
    matchinator: Matchinator = Matchinator(rejects, orderable)
    file_name = matchinator.create_match_workbook()
    
    if file_name:
        st.download_button(label="Télécharger le fichier", 
                           data=open(file_name, "rb").read(), file_name=file_name)