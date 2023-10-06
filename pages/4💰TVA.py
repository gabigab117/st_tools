import streamlit as st


st.set_page_config(page_title="Outil TVA", page_icon="💰")

st.write("Appli permettant de calculer le prix de vente HT ou TTC")

option = st.radio("Vous voulez calculer le prix HT ou TTC ? ", 
               ("TTC", "HT"))

if option =="TTC":
    st.write("Vous avez le prix HT et vous voulez calculer le prix TTC")

    tva = st.radio("Quel est le taux de TVA ?", (5.5, 10, 20))
    ht = st.number_input("Prix HT : ")
    ttc = ht * (1+(tva/100))

    st.write(f"Prix TTC = {round(ttc, 4)}")

else:
    st.write("Vous avez le prix TTC et vous voulez calculer le prix HT")

    tva = st.radio("Quel est le taux de TVA ?", (5.5, 10, 20))
    ttc = st.number_input("Prix TTC :")

    ht = ttc/(1+(tva/100))
    
    st.write(f"Prix HT = {round(ht, 4)}")