# Fonctionnalités à ajouter : le coeff se calcule en fonction du PV renseigné
import streamlit as st


st.set_page_config(page_icon="✍", page_title="Pv avec coefficient")
st.write("Appli permettant de calculer le PV en fonction d'un coefficient")


with st.expander(label="Calculer le PV à partur du coefficient"):
    pa = st.number_input(label="Prix d'achat", help="PA HT")
    coeff = st.number_input(label="Coefficient", help="Exemple : 1,5 / 1,8")

    if pa and coeff:
        pv = pa*coeff
        st.write(f"PA de {pa}€ avec un coef de {coeff} : Prix de vente TTC = {round(pv, 2)}€")

        tva = st.radio(label="TVA", 
                    options=[5.5, 10, 20])
        pvht = pv/(1+(tva/100))
        marge = pvht - pa
        st.write(f"Marge de {round(marge, 2)}€")
        tx = (marge/pvht)*100
        st.write(f"Soit : {round(tx, 2)} %")

