import streamlit as st
from pymongo import MongoClient
import pandas as pd
import certifi

st.title('Prueba de conexión a MongoDB')

@st.cache_resource()
def connection():
    return MongoClient('mongodb+srv://'+st.secrets["DB_USERNAME"]+':'+st.secrets["DB_PASSWORD"]+',@prediccion2024.q7xsfjw.mongodb.net/')

conexion = connection()

@st.cache_data(ttl=60)
def getData():
    db = conexion.get_database('sample_restaurants')
    collection = db.get_collection('restaurants')
    items = collection.find()
    return list(items)

def insertData(newData):
    db = conexion.get_database('sample_restaurants')
    nuevaCollection = db.get_collection('inventario')
    nuevaCollection.insert_many(newData)

datos = getData()
st.write(datos)
st.dataframe(pd.DataFrame(datos))

#Vamos a guardar una nueva collection en la base de datos

dfInventory = pd.read_csv("datos/inventory.csv")
st.dataframe(dfInventory.head())

inventoryCollection = dfInventory.to_dict(orient="records")
st.write(inventoryCollection[0:3])
insertData(inventoryCollection)

