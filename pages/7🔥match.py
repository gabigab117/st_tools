import streamlit as st
from func import Matchinator

st.set_page_config(page_title="Rejets", page_icon="🔥")


rejects = st.file_uploader("Rejets", type=["xlsx"])
orderable = st.file_uploader("Cadencier", type=["xlsx"])
user = st.text_input(label="Prénom", max_chars=20)


if rejects and orderable and user:
    with st.spinner("Patience..."):
        matchinator: Matchinator = Matchinator(rejects, orderable, user)
        file_name = matchinator.create_match_workbook()
    
    if file_name:
        st.download_button(label="Télécharger le fichier", 
                        data=open(file_name, "rb").read(), file_name=file_name)