# 📊 Proyecto Integrador: Minería de Datos I
### Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial (ITSE)

Este repositorio contiene el desarrollo del **Trabajo Final Integrador** para la asignatura Minería de Datos I. El proyecto implementa un pipeline completo de procesamiento de datos, desde la inspección de un dataset crudo en formato JSON, su correspondiente limpieza, análisis exploratorio estadístico, reducción de dimensionalidad mediante PCA, hasta la comunicación de resultados a través de una aplicación interactiva.

---

## 👥 Integrantes
* **Carrizo, José Luis**
* **Barraza, José Martín**

---

## 📁 Estructura y Trazabilidad del Repositorio

Cumpliendo con los requisitos de orden y reproducibilidad exigidos por la cátedra, la estructura del proyecto está organizada de la siguiente manera:

```text
PI_MINERIA_DATOS_1/
├── app/
│   ├── Home.py                 # Página principal del Tablero Interactiva
│   └── pages/
│       ├── 01_Dataset.py       # Etapa 1: Inspección y calidad de datos crudos
│       ├── 02_EDA.py           # Etapa 2: Análisis Exploratorio (Uni/Bi/Multivariado)
│       ├── 03_PCA.py           # Etapa 3: Escalamiento y Componentes Principales
│       └── 04_Conclusiones.py  # Etapa 4: Hallazgos estratégicos del negocio
├── data/
│   ├── raw/                    # Dataset original provisto por la cátedra (JSON)
│   └── processed/              # Dataset modificado mediante limpieza justificada (CSV)
├── notebooks/                  # Jupyter Notebooks utilizados para la experimentación inicial
├── requirements.txt            # Archivo de dependencias y librerías del entorno
└── README.md                   # Documentación principal obligatoria del repositorio