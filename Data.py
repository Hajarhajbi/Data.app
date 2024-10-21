import streamlit as st
import pandas as pd
st.title("MY Application Streamlit ")
st.write("Upload your CSV file for a complete statistical analysis.")
st.title("Charger et utiliser un fichier Excel avec Pandas")
uploaded_file = st.file_uploader("Choisissez un fichier Excel", type=["xlsx"])
if uploaded_file is not None:
     df = pd.read_excel(uploaded_file)
     st.write("Voici les premières lignes du fichier :")
     st.write(df.head())
     st.write("Statistiques descriptives :")
     st.write(df.describe())
     

