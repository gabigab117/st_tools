import streamlit as st
from func import Matchinator, NonReferencedMatchinator

st.set_page_config(page_title="Rejets + cadencier", page_icon="🔥")

st.title("Veuillez sléctionner une option : ")
choice = st.radio(label="Source", 
                    options=["Cadencier Casino", "Casino non ref dans METI"])

rejects = st.file_uploader("Rejets", type=["xlsx"])
orderable = st.file_uploader("Cadencier", type=["xlsx"])
user = st.text_input(label="Prénom", max_chars=20)


if rejects and orderable and user:
    if choice == "Cadencier":
        matchinator: Matchinator = Matchinator(rejects, orderable, user)
    else:
        matchinator: NonReferencedMatchinator = NonReferencedMatchinator(rejects, orderable, user)
    file_name = matchinator.create_match_workbook()
    
    if file_name:
        st.download_button(label="Télécharger le fichier", 
                        data=open(file_name, "rb").read(), file_name=file_name)