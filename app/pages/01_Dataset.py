import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="Inspección del Dataset", layout="wide")
st.title("Etapa 1: Inspección y Calidad del Dataset")
st.markdown("---")

ruta_dirty = os.path.join("data", "raw", "streaming_users_dirty.json")
ruta_clean = os.path.join("data", "processed", "dataset_procesado.csv")

@st.cache_data
def cargar_datos_raw():
    for r in [ruta_dirty, os.path.join("data", "streaming_users_dirty.json")]:
        if os.path.exists(r):
            with open(r, "r", encoding="utf-8") as f:
                return pd.DataFrame(json.load(f))
    return None

@st.cache_data
def cargar_datos_clean():
    if os.path.exists(ruta_clean):
        return pd.read_csv(ruta_clean)
    return None

df_dirty = cargar_datos_raw()
df_clean = cargar_datos_clean()

st.subheader("1. Estado Inicial de los Datos (JSON Crudo)")
if df_dirty is not None:
    st.markdown(f"El dataset crudo original contiene **{df_dirty.shape[0]:,}** registros.")
    st.dataframe(df_dirty.head(5))
else:
    st.warning("No se pudo hallar el archivo original.")

st.markdown("---")

st.subheader("2. Dataset Definitivo Procesado")
if df_clean is not None:
    st.success(f"¡Dataset procesado conectado con éxito! Contiene **{df_clean.shape[0]:,}** usuarios.")
    st.write("Vista previa de los datos listos para el análisis:")
    st.dataframe(df_clean.head(5))
else:
    st.error("Alerta: No se encontró el archivo 'dataset_procesado.csv' en la carpeta data/processed/")