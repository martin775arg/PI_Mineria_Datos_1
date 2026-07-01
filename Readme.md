# 📊 Proyecto Integrador: Minería de Datos I
### Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial (ITSE)

---

## ● Información general
* **Institución:** Instituto Tecnológico Santiago del Estero (ITSE).
* **Asignatura:** Minería de Datos I.
* **Año:** 2026.
* **Integrantes:** 
  * Carrizo, José Luis
  * Barraza, José Martín
* **Enlace a la aplicación pública:** [Tablero de Streamlit Cloud](https://share.streamlit.io/) *(Reemplazar con tu enlace funcional)*
* **Enlace al repositorio público:** [Repositorio GitHub](https://github.com/) *(Reemplazar con tu enlace funcional)*

---

## ● Objetivo del proyecto
El propósito central de este Proyecto Integrador consiste en desarrollar un análisis de datos reproducible y comunicable a partir del dataset provisto por la cátedra. Se busca aplicar las herramientas de Minería de Datos I para construir un pipeline trazable con decisiones debidamente justificadas mediante evidencia observada. El alcance incluye la inspección inicial, calidad de datos, preparación, análisis exploratorio, escalamiento y reducción de dimensionalidad. No contempla modelado predictivo ni el despliegue de modelos de Machine Learning. El foco principal está puesto en la coherencia entre etapas y la claridad para comunicar los resultados obtenidos.

---

## ● Dataset
El dataset original está preservado sin modificaciones en la ruta `data/raw/` en formato JSON. Representa un conjunto de registros orientados a usuarios y sus interacciones dentro de una plataforma de streaming. Cuenta con variables de tipo numérico, categórico y temporal que describen perfiles, consumo y comportamiento. En la fase inicial se evaluaron las dimensiones, tipos de datos, presencia de nulos y duplicados en el notebook `01_inspeccion_inicial.ipynb`. Esta inspección permitió reunir la evidencia necesaria para guiar las transformaciones posteriores sin alterar el origen.

---

## ● Estructura del repositorio
Siguiendo las pautas estructurales obligatorias impuestas por la cátedra, el repositorio se organiza de la siguiente manera:

```text
PI_Mineria_Datos_1/
├── README.md                   # Documentación técnica principal del proyecto
├── requirements.txt            # Declaración de dependencias del entorno
├── data/
│   ├── raw/                    # Dataset original sin modificaciones (JSON)
│   └── processed/              # Dataset final utilizado en el análisis (CSV)
├── notebooks/                  # Desarrollo ordenado de las etapas del proyecto
│   ├── 01_inspeccion_inicial.ipynb
│   ├── 02_calidad_y_limpieza.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_pca.ipynb
│   └── 05_conclusiones.ipynb
├── app/                        # Aplicación pública interactiva
│   ├── Home.py                 # Página principal del tablero
│   └── pages/
│       ├── 01_Dataset.py       # Vista previa y calidad del dataset
│       ├── 02_EDA.py           # Visualizaciones exploratorias interpretadas
│       ├── 03_PCA.py           # Configuración y resultados del modelo PCA
│       └── 04_Conclusiones.py  # Reporte de hallazgos y limitaciones
├── reports/
│   └── informe_final.pdf       # Informe final ejecutivo breve (máximo 2 páginas)
└── logs/
    └── pipeline_log.csv        # Registro histórico de transformaciones ETL
```



## ● Preparación y calidad de datos
Las etapas de limpieza se encuentran documentadas exhaustivamente en el archivo 02_calidad_y_limpieza.ipynb. Las decisiones de preparación surgieron directamente de la evidencia observada en la inspección. Se eliminaron registros duplicados y se aplicaron estrategias justificadas para el tratamiento de valores faltantes. Cada transformación relevante quedó guardada en logs/pipeline_log.csv, detallando la descripción de la acción, número de filas resultantes, nulos remanentes y el porcentaje de retención. El dataset depurado final se exportó a data/processed/
## ●Resumen del análisis exploratorio
Desarrollado en 03_eda.ipynb, el análisis abarcó visualizaciones univariadas, bivariadas y multivariadas. Se estudiaron las distribuciones individuales de las variables críticas de consumo y se cruzaron factores de comportamiento. Cada visualización incluye una interpretación explícitamente conectada con los objetivos del negocio. Las observaciones permitieron detectar patrones de comportamiento, correlaciones entre variables numéricas y la estructura de los segmentos de usuarios antes de proceder al modelado estadístico.
## ●Reducción de dimensionalidad
Ubicado en 04_pca.ipynb, se documentó el uso del Análisis de Componentes Principales. El proceso inició seleccionando las variables numéricas adecuadas y aplicando un escalamiento y estandarización estadística indispensable para el algoritmo. Se calculó el porcentaje de varianza explicada por cada componente para definir el número óptimo de dimensiones. El resultado permite simplificar la estructura de los datos interpretando el peso y propósito de cada componente dentro del análisis global.

## ●Visualización interactiva
La comunicación de resultados se implementó en una aplicación pública desplegada en Streamlit Cloud[cite: 1]. El tablero incluye:

Home: Presentación, integrantes y enlace directo al repositorio de GitHub.

Dataset: Descripción de variables, resumen de calidad y mención de transformaciones.

EDA: Exactamente 5 gráficos interactivos (2 univariados, 2 bivariados, 1 multivariado) acompañados de su respectiva interpretación técnica.

PCA: Explicación de variables, escalamiento, varianza acumulada y gráficos asociados.

Conclusiones: Reporte dinámico orientado al público general