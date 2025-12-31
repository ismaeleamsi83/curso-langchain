# Documentación: Tema 2/cv_analyzer/ui/streamlit_ui.py

Este documento describe el propósito y funcionamiento del archivo `streamlit_ui.py`.

## Descripción General
Este archivo define la interfaz de usuario (UI) completa de la aplicación **CV Analyzer** utilizando **Streamlit**. Gestiona la carga de archivos, la entrada de texto por parte del usuario y la visualización de los resultados del análisis de la IA.

## Funcionalidades Clave
- **Layout de Dos Columnas**: Divide la pantalla en una sección de entrada y otra de resultados.
- **Visualización de Proceso**: Implementa barras de progreso y mensajes de estado (`st.spinner`, `st.progress`) para guiar al usuario durante el análisis.
- **Métricas Visuales**: Utiliza `st.metric` para resaltar el porcentaje de ajuste al puesto con códigos de colores (verde, amarillo, naranja, rojo).
- **Componentes de UI Dinámicos**: Muestra alertas, botones de guardado y resúmenes estructurados mediante el uso de `st.info`, `st.success` y `st.divider`.

## Lógica de UI
- `main()`: Configura la página y orquestra las columnas.
- `procesar_entrada()`: Captura el PDF y la descripción del puesto.
- `mostrar_resultados()`: Mapea el objeto `AnalisisCV` a componentes visuales de Streamlit.

## Código Fuente
```python
# (El código fuente es extenso y se encuentra en el archivo original)
# A continuación se muestra un resumen de la estructura principal:

import streamlit as st
from models.cv_model import AnalisisCV
from services.pdf_processor import extraer_texto_pdf
from services.cv_evaluator import evaluar_candidato

def main():
    st.set_page_config(page_title="Sistema de Evaluación de CVs", page_icon="📄", layout="wide")
    st.title("📄 Sistema de Evaluación de CVs con IA")
    
    col_entrada, col_resultado = st.columns([1, 1], gap="large")
    
    with col_entrada:
        procesar_entrada()
    
    with col_resultado:
        mostrar_area_resultados()

# ... (resto de funciones de ayuda)
```
> [!NOTE]
> El código fuente completo de este archivo supera las 270 líneas y define toda lo interactividad de la aplicación.
