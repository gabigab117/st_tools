import streamlit as st
import os

from func import check_password

st.set_page_config(page_icon="🏴‍☠️", page_title="Administration")
st.write("Administration")

if check_password():
    with st.expander("Nettoyer les images"):
        del_img = st.toggle("Supprimer les images")
        if del_img:
            actual_rep = os.getcwd()
            files = os.listdir(path=actual_rep)
            for file in files:
                _, ext = os.path.splitext(file)
                if ext == '.png':
                    os.remove(file)
