# Documentación: Tema 2/cv_analyzer/services/pdf_processor.py

Este documento describe el propósito y funcionamiento del archivo `pdf_processor.py`.

## Descripción General
Este servicio se encarga de la extracción de texto desde archivos PDF subidos por el usuario. Es el primer paso en la tubería de análisis de CVs.

## Funcionalidades Clave
- **PyPDF2**: Utiliza esta librería para leer y extraer el contenido de las páginas del PDF.
- **BytesIO**: Permite manejar el archivo PDF en memoria sin necesidad de guardarlo en el disco.
- **Marcado de Páginas**: Agrega un encabezado informativo (`--- PÁGINA X ---`) para cada página extraída, lo que ayuda a mantener el contexto del documento original.
- **Validación de Contenido**: Detecta si el archivo PDF está vacío o si contiene solo imágenes (donde la extracción de texto simple fallaría).

## Código Fuente
```python
import PyPDF2
from io import BytesIO

def extraer_texto_pdf(archivo_pdf):
    try:
        pdf_reader = PyPDF2.PdfReader(BytesIO(archivo_pdf.read()))
        texto_completo = ""

        for numero_pagina, pagina in enumerate(pdf_reader.pages, 1):
            texto_pagina = pagina.extract_text()
            if texto_pagina.strip():
                texto_completo += f"\n--- PÁGINA {numero_pagina} ---\n {texto_pagina} \n"
    
        texto_completo = texto_completo.strip()
        
        if not texto_completo:
            return "Error: El PDF parece estar vacío o contener solo imágenes."

        return texto_completo

    except Exception as e:
        return f"Error al procesar el archivo PDF: {str(e)}"
```
