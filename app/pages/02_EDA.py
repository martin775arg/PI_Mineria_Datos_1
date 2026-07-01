import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Gráficos EDA - PI", layout="wide")
st.title("Etapa 2: Análisis Exploratorio de Datos (EDA)")
st.markdown("---")

@st.cache_data
def cargar_datos():
    ruta = os.path.join("data", "processed", "dataset_procesado.csv")
    if os.path.exists(ruta):
        return pd.read_csv(ruta)
    return None

df_clean = cargar_datos()

if df_clean is not None:
    
    st.subheader("Visualizaciones Estadísticas del Comportamiento del Negocio")
    st.markdown("A continuación se presentan los 5 gráficos estructurales que describen el ecosistema de los usuarios de streaming.")
    
    # -------------------------------------------------------------
    # FILA 1: Gráficos 1 y 2 (Distribuciones Numéricas)
    # -------------------------------------------------------------
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Gráfico 1: Distribución de Edades (`age`)**")
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        sns.histplot(df_clean['age'], kde=True, color='purple', bins=20, ax=ax1)
        ax1.set_xlabel("Edad (Años)")
        ax1.set_ylabel("Cantidad de Usuarios")
        st.pyplot(fig1)
        
    with col2:
        st.markdown("**Gráfico 2: Tiempo de Consumo Mensual (`monthly_watch_time_mins`)**")
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        sns.histplot(df_clean['monthly_watch_time_mins'], kde=True, color='blue', bins=20, ax=ax2)
        ax2.set_xlabel("Minutos al Mes")
        ax2.set_ylabel("Frecuencia")
        st.pyplot(fig2)

    st.markdown("---")

    # -------------------------------------------------------------
    # FILA 2: Gráficos 3 y 4 (Soporte Técnico y Géneros)
    # -------------------------------------------------------------
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("**Gráfico 3: Volumen de Reclamos (`customer_support_tickets`)**")
        fig3, ax3 = plt.subplots(figsize=(6, 4))
        sns.countplot(data=df_clean, x='customer_support_tickets', palette='viridis', ax=ax3)
        ax3.set_xlabel("Cantidad de Tickets por Usuario")
        ax3.set_ylabel("Casos Registrados")
        st.pyplot(fig3)
        
    with col4:
        st.markdown("**Gráfico 4: Preferencia de Géneros Audiovisuales (`favorite_genre`)**")
        fig4, ax4 = plt.subplots(figsize=(6, 4))
        # Ordenamos las barras de mayor a menor para que quede prolijo
        orden_generos = df_clean['favorite_genre'].value_counts().index
        sns.countplot(data=df_clean, x='favorite_genre', palette='rocket', order=orden_generos, ax=ax4)
        ax4.set_xlabel("Género Favorito")
        ax4.set_ylabel("Usuarios")
        plt.xticks(rotation=45)
        st.pyplot(fig4)

    st.markdown("---")

    # -------------------------------------------------------------
    # FILA 3: Gráfico 5 Centrado (Planes de Suscripción)
    # -------------------------------------------------------------
    st.markdown("**Gráfico 5: Distribución por Plan de Suscripción (`subscription_plan`)**")
    fig5, ax5 = plt.subplots(figsize=(8, 3.5))
    orden_planes = df_clean['subscription_plan'].value_counts().index
    sns.countplot(data=df_clean, x='subscription_plan', palette='magma', order=orden_planes, ax=ax5)
    ax5.set_xlabel("Tipo de Plan")
    ax5.set_ylabel("Total de Usuarios")
    st.pyplot(fig5)

else:
    st.error("No se pudo cargar el archivo 'dataset_procesado.csv' en la ruta data/processed/.")