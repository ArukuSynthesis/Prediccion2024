from pymongo import MongoClient
import pandas as pd
import streamlit as st
import requests

#Conectar a MongoDB usando de database.py el método connection()

client = MongoClient('mongodb+srv://'+st.secrets["DB_USERNAME"]+':'+st.secrets["DB_PASSWORD"]+'@prediccion2024.q7xsfjw.mongodb.net/?retryWrites=true&w=majority&appName=Prediccion2024')
db = client["sample_restaurants"]

#Obtener datos de la base de datos
@st.cache_data(hash_funcs={MongoClient: id})
def load_data(collection):
    data = list(db[collection].find())
    return data

#Crear una barra lateral para acceder a los datos
st.sidebar.subheader("MongoDB:")
collection = st.sidebar.selectbox("Selecciona una colección: ", db.list_collection_names())

#Cargar la collección seleccionada
if collection:
    data = load_data(collection)
    df = pd.DataFrame(data)

    #Mostrar los datos
    st.write("Mostrando datos de la colección: ", collection)
    st.dataframe(df)
