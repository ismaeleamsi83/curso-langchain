# Documentación: Tema 2/cv_analyzer/app.py

Este documento describe el propósito y funcionamiento del archivo `app.py` dentro del proyecto `cv_analyzer`.

## Descripción General
Este es el punto de entrada principal para la aplicación **CV Analyzer**. Su única responsabilidad es importar y ejecutar la función principal de la interfaz de usuario definida en `ui/streamlit_ui.py`.

## Funcionalidades Clave
- **Punto de Entrada**: Facilita la ejecución de la aplicación mediante el comando `streamlit run app.py`.
- **Modularización**: Separa la ejecución de la lógica de la interfaz.

## Código Fuente
```python
import streamlit as st
from ui.streamlit_ui import main

if __name__ == "__main__":
    main()
```
