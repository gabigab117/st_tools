import streamlit as st
import openfoodfacts

# 5449000000996


st.set_page_config(page_title="Base de produits", page_icon="🌳")


api = openfoodfacts.API(user_agent="Streamlit tools")

with st.expander("Rechercher avec un EAN"):
    ean = st.text_input(label="EAN produit")
    if ean:
        product = api.product.get(ean, fields=["code", "product_name", "packaging"])
        st.write(f"{product['code']} -- {product['product_name']}")
        st.write(product["packaging"])
        st.write(product)
