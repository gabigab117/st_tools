import streamlit as st
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt


st.set_page_config(page_title="DataFrame", page_icon="🔥")

st.write("Lecteur Excel")

data = st.file_uploader("Fichier Excel")


if data:
    df = pd.read_excel(data, header=0)

    with st.expander("Afficher le tableau"):
        st.dataframe(df)