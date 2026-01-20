import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(layout="wide")

# Chargement des données
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
df = pd.read_csv(url)

# fonction de correspondance
def image_ville(nom_ville):
    links = {
        "Manhattan": "https://raw.githubusercontent.com/akouvi-lab/projet_streamlit/refs/heads/main/image_manathan.jfif",
        "Queens": "https://raw.githubusercontent.com/akouvi-lab/projet_streamlit/999564601e5344a6394ac95626a39960dac74d4e/image_queen.jpg",
        "Brooklyn": "https://raw.githubusercontent.com/akouvi-lab/projet_streamlit/999564601e5344a6394ac95626a39960dac74d4e/image_Brooklyn.jfif",
        "Bronx": "https://raw.githubusercontent.com/akouvi-lab/projet_streamlit/999564601e5344a6394ac95626a39960dac74d4e/image_Bronx.jfif",
        "nan": "https://raw.githubusercontent.com/akouvi-lab/projet_streamlit/main/point_d'interrogation.png"
    }
    return links.get(nom_ville)

#st.title("🚖 Bienvenue sur le site web de Akouvi")

# Les quartiers pour l'affichage initial de la grille
villes_grille = ["Manhattan", "Queens", "Brooklyn", "Bronx"]

# Création de la grille 2x2
for i in range(0, len(villes_grille), 2):
    cols = st.columns(2)
    
    for j in range(2):
        quartier_par_defaut = villes_grille[i + j]
        
        with cols[j]:
            #st.subheader(f"Secteur {quartier_par_defaut}")
            st.title("🚖 Bienvenue sur le site web de Akouvi")
            
            # --- LA LISTE DÉROULANTE AVEC LES ARRONDISSEMENTS ---
            # récupèration de la liste de tous les arrondissements possibles dans le DF
            liste_arrondissements = df["pickup_borough"].dropna().unique().tolist()
            # On ajoute "nan" manuellement à la liste des choix
            liste_arrondissements.append("nan")
            
            # L'utilisateur peut choisir n'importe quel arrondissement dans chaque bloc
            choix = st.selectbox(
                "Indiquer votre arrondissement de récupération:", 
                options=liste_arrondissements, 
                index=liste_arrondissements.index(quartier_par_defaut), # Positionne le curseur sur le bon quartier par défaut
                key=f"select_{quartier_par_defaut}"
            )
            
            st.write(f"📍 Tu as choisis : **{choix}**")
            
            # L'image change DYNAMIQUEMENT selon le choix dans la selectbox
            url_img = image_ville(choix)
            st.image(url_img, use_container_width=True, output_format="auto", width=400)
