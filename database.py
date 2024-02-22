import streamlit as st
from pymongo import MongoClient

st.title('Prueba de conexión a MongoDB')

def connection():
    return MongoClient('mongodb+srv://alexhernandezcastro00:iXlxlLLhvBQykiBO@prediccion2024.q7xsfjw.mongodb.net/')

conexion = connection()

def getData():
    db = conexion.get_database('sample_restaurants')
    collection = db.get_collection('restaurants')
    items = collection.find()
    return list(items)

datos = getData()
st.write(datos)