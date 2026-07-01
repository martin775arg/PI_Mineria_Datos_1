import streamlit as st

st.set_page_config(page_title="Conclusiones Estratégicas - PI", layout="wide")
st.title("Etapa 4: Conclusiones y Plan de Acción Estratégico")
st.markdown("---")

st.subheader("Traducción del Modelo de Datos a Decisiones de Negocio")
st.markdown("""
El Análisis de Componentes Principales (PCA) permitió reducir la dimensionalidad de las métricas de comportamiento de los usuarios, aislando el ruido estadístico y demostrando una distribución homogénea de la varianza. 

A partir de esta estructura matemática, se convalidan tres líneas de acción comercial y operativa aplicadas a cada uno de los Perfiles Latentes identificados:
""")

# Estructuración en pestañas interactivas para una navegación profesional
tab1, tab2, tab3 = st.tabs([
    "PC1: Consumo Orgánico Maduro", 
    "PC2: Fricción Operativa Administrativa", 
    "PC3: Consumo Joven Intensivo"
])

with tab1:
    st.markdown("### Perfil Latente 1: Consumo Orgánico Maduro")
    st.markdown("""
    **Diagnóstico Analítico:** Representa a usuarios adultos con una tasa de uso estable y un volumen de interacciones con el servicio de soporte técnico dentro de los parámetros estándar.
    
    **Plan de Acción Comercial:**
    * **Fidelización Orgánica:** Implementar campañas de retención pasivas basadas en la estabilidad de su facturación histórica.
    * **Recomendaciones de Catálogo:** Optimizar los algoritmos de sugerencias orientados a géneros tradicionales o de consumo pausado (ej. Documentales y Drama), maximizando el tiempo de permanencia sin saturar la interfaz de usuario.
    """)

with tab2:
    st.markdown("### Perfil Latente 2: Fricción Operativa Administrativa")
    st.markdown("""
    **Diagnóstico Analítico:** Este perfil concentra la varianza asociada a un volumen elevado de reclamos y tickets de soporte técnico, detectándose principalmente en segmentos de usuarios de mayor edad.
    
    **Plan de Acción Operativo (Mitigación de Churn):**
    * **Rediseño de Accesibilidad (UX/UI):** Simplificar los flujos de navegación críticos dentro de la plataforma (como las secciones de pago, actualización de datos fiscales y renovación de planes de suscripción) para adaptarlos a adultos mayores.
    * **Optimización de Canales de Soporte:** Establecer un canal prioritario de resolución automatizada o asistencia guiada para reducir el tiempo de espera en los reclamos y resolver la fricción administrativa antes de que provoque la baja del servicio.
    """)

with tab3:
    st.markdown("### Perfil Latente 3: Consumo Joven Intensivo")
    st.markdown("""
    **Diagnóstico Analítico:** Representa a la masa crítica de clientes jóvenes con un uso intensivo de la plataforma (alto volumen de minutos mensuales) pero con nula o muy baja interacción con el área de soporte técnico.
    
    **Plan de Acción Estratégico:**
    * **Estrategias de Retención Gamificadas:** Desarrollar sistemas de fidelización dinámicos (como logros por maratones de series o accesos anticipados a estrenos de géneros de alta demanda como Acción o Thriller).
    * **Upselling enfocado en Infraestructura:** Dirigir las campañas de actualización de planes (Premium) destacando las mejoras tecnológicas (calidad de transmisión 4K, múltiples pantallas simultáneas y audio envolvente) en lugar de centrar la estrategia en la cantidad de títulos del catálogo.
    """)

st.markdown("---")
st.success("¡Pipeline de la aplicación Streamlit finalizado con éxito! El proyecto se encuentra completamente integrado y listo para su defensa académica.")