import streamlit as st
import cowsay


st.set_page_config(page_title="Index", page_icon="🛠"
                   )

st.text(cowsay.get_output_string("fox", "Boite à outils du magasin, la seléction se fait par le menu de gauche."))
