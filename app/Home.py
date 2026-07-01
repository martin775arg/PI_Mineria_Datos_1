import streamlit as st
import pandas as pd
import os

# Configuración de la página oficial de la cátedra
st.set_page_config(
    page_title="Trabajo Práctico Integrador - Minería de Datos I",
    layout="wide"
)

st.title("Trabajo Práctico Integrador - Minería de Datos I")
st.subheader("Estructuración de Perfiles Latentes en Plataformas de Streaming")
st.markdown("---")

# Presentación Institucional
st.markdown("""
### Bienvenido al Tablero de Control Estratégico

Este desarrollo interactivo complementa el pipeline de análisis matemático realizado en el laboratorio de notebooks. 
El objetivo principal del proyecto es aplicar técnicas avanzadas de **Minería de Datos** para identificar el comportamiento de los usuarios y construir perfiles analíticos que optimicen la toma de decisiones comerciales.

**Estructura del Proyecto del Tablero:**
1. **Inspección y Limpieza:** Calidad de datos sobre el JSON original.
2. **EDA:** Análisis exploratorio mediante visualizaciones univariadas y bivariadas.
3. **Modelo PCA:** Reducción de dimensionalidad y análisis de varianza ortogonal.
4. **Conclusiones:** Recomendaciones y planes de acción estratégica.
""")

st.markdown("---")

# Verificación de carga de datos nativa
@st.cache_data
def cargar_resumen_datos():
    # Recordá que en Streamlit las rutas se leen paradas desde la raíz del proyecto
    ruta = os.path.join("data", "processed", "dataset_procesado.csv")
    if os.path.exists(ruta):
        return pd.read_csv(ruta)
    return None

df_clean = cargar_resumen_datos()

if df_clean is not None:
    st.success("¡Base de datos procesada conectada con éxito al tablero!")
    
    # Métricas clave de tu dataset real
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric(label="Total de Usuarios Analizados", value=f"{df_clean.shape[0]:,}")
    with col_m2:
        st.metric(label="Variables de Comportamiento", value=f"{df_clean.shape[1]}")
    with col_m3:
        st.metric(label="Variables en Modelo PCA", value="3 (Nativas)")
        
else:
    st.error("Alerta: No se encontró el archivo 'dataset_procesado.csv' en la ruta 'data/processed/'. Verificá la estructura de directorios.")