import streamlit as st
import pandas as pd
import os

# Configuración de la página
st.set_page_config(
    page_title="Minería de Datos I - Proyecto Integrador",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para una estética premium y moderna
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');
    
    /* Configuración global de fuentes */
    .stApp {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Encabezado principal */
    .header-container {
        padding: 2.5rem;
        background: linear-gradient(135deg, #1e1b4b 0%, #311042 100%);
        border-radius: 16px;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
    }
    
    .header-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(to right, #a5b4fc, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        line-height: 1.2;
    }
    
    .header-subtitle {
        font-size: 1.1rem;
        font-weight: 400;
        color: #cbd5e1;
        margin-top: 0.75rem;
        margin-bottom: 0;
    }

    /* Tarjetas de Información */
    .info-card {
        background-color: rgba(30, 41, 59, 0.03);
        border: 1px solid rgba(226, 232, 240, 0.8);
        border-radius: 12px;
        padding: 1.5rem;
        height: 100%;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    
    /* Modo oscuro compatible */
    @media (prefers-color-scheme: dark) {
        .info-card {
            background-color: rgba(30, 41, 59, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.05);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
        }
    }
    
    .info-title {
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 1rem;
        color: #4f46e5;
    }
    
    @media (prefers-color-scheme: dark) {
        .info-title {
            color: #818cf8;
        }
    }

    .info-item {
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
        line-height: 1.5;
    }
    
    /* Botón de Github */
    .github-link-container {
        margin-top: 1.5rem;
        text-align: left;
    }
    
    .github-btn {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        color: #ffffff !important;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        text-decoration: none !important;
        transition: all 0.2s ease-in-out;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    .github-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(79, 70, 229, 0.2);
        border-color: rgba(129, 140, 248, 0.4);
    }
    
    .github-btn svg {
        fill: currentColor;
    }
</style>
""", unsafe_allow_html=True)

# 1. Banner Principal de Bienvenida
st.markdown("""
<div class="header-container">
    <div class="header-title">Estructuración de Perfiles Latentes en Plataformas de Streaming</div>
    <div class="header-subtitle">Trabajo Final Integrador — Minería de Datos I</div>
</div>
""", unsafe_allow_html=True)

# 2. Layout Principal: Información Institucional y del Repositorio
col_left, col_right = st.columns([1, 1.2], gap="large")

with col_left:
    st.markdown("""
    <div class="info-card">
        <div class="info-title">📋 Detalles del Proyecto</div>
        <div class="info-item"><strong>Institución:</strong> Instituto Tecnológico Santiago del Estero (ITSE)</div>
        <div class="info-item"><strong>Carrera:</strong> Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial</div>
        <div class="info-item"><strong>Asignatura:</strong> Minería de Datos I</div>
        <div class="info-item"><strong>Comisión:</strong> Turno Tarde</div>
        <div class="info-item"><strong>Fecha:</strong> Julio 2026</div>
        <hr style="margin: 1rem 0; border: 0; border-top: 1px solid rgba(128,128,128,0.2);">
        <div class="info-title">👥 Integrantes</div>
        <div class="info-item">👤 <strong>Carrizo, José Luis</strong></div>
        <div class="info-item">👤 <strong>Barraza, José Martín</strong></div>
        <hr style="margin: 1rem 0; border: 0; border-top: 1px solid rgba(128,128,128,0.2);">
        <div class="info-title">🌐 Repositorio del Proyecto</div>
        <div class="info-item">Accede al código fuente completo, notebooks de desarrollo y documentación técnica en GitHub.</div>
        <div class="github-link-container">
            <a href="https://github.com/martin775arg/PI_Mineria_Datos_1" target="_blank" class="github-btn">
                <svg height="20" width="20" viewBox="0 0 16 16">
                    <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
                Ver en GitHub
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
    <div class="info-card">
        <div class="info-title">💡 Contexto y Propósito</div>
        <p style="font-size: 0.98rem; line-height: 1.6; margin-bottom: 1.2rem;">
            Este Tablero de Control Estratégico es una herramienta interactiva diseñada para comunicar los resultados del pipeline de análisis de datos. 
            El objetivo principal es identificar <strong>perfiles de comportamiento latente</strong> en los usuarios de plataformas de streaming a partir del dataset provisto por la cátedra.
        </p>
        <p style="font-size: 0.98rem; line-height: 1.6; margin-bottom: 1.2rem;">
            A lo largo de las distintas secciones accesibles desde el panel lateral, se despliega el análisis reproducible, la justificación de las decisiones tomadas sobre los datos y la evidencia empírica que soporta nuestras conclusiones.
        </p>
        <div class="info-title">🧭 Secciones del Tablero</div>
        <ul style="font-size: 0.95rem; line-height: 1.6; margin-left: -1rem;">
            <li><strong>01. Dataset:</strong> Inspección de la calidad inicial de datos y resumen del proceso de limpieza ETL.</li>
            <li><strong>02. EDA:</strong> Análisis Exploratorio de Datos con 5 visualizaciones interactivas interpretadas en detalle.</li>
            <li><strong>03. PCA:</strong> Estandarización de variables, análisis de varianza explicada y visualizaciones del modelo de reducción de dimensionalidad.</li>
            <li><strong>04. Conclusiones:</strong> Hallazgos clave identificados, limitaciones inherentes al estudio y próximos pasos sugeridos.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 3. Verificación de carga de datos y métricas
@st.cache_data
def cargar_resumen_datos():
    ruta = os.path.join("data", "processed", "dataset_procesado.csv")
    if os.path.exists(ruta):
        try:
            return pd.read_csv(ruta)
        except Exception as e:
            st.error(f"Error al leer el dataset procesado: {e}")
    return None

df_clean = cargar_resumen_datos()

if df_clean is not None:
    st.success("✨ ¡Conexión exitosa con la base de datos procesada!")
    
    # Métricas del dataset con estilo mejorado
    st.markdown("### 📊 Métricas Clave del Dataset Procesado")
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric(label="Total de Usuarios Analizados", value=f"{df_clean.shape[0]:,}")
    with col_m2:
        st.metric(label="Variables de Comportamiento", value=f"{df_clean.shape[1]}")
    with col_m3:
        st.metric(label="Variables en Modelo PCA", value="3 (Nativas)")
else:
    st.warning("⚠️ Nota: No se detectó el archivo 'dataset_procesado.csv' en 'data/processed/'. Por favor, asegúrate de ejecutar el notebook de calidad y limpieza para generar el dataset procesado.")