# Documentación: Tema 2/output_parsers_modo_actual.py

Este documento describe el propósito y funcionamiento del archivo `output_parsers_modo_actual.py`.

## Descripción General
Este archivo es una guía exhaustiva sobre el uso de `.with_structured_output()` en LangChain. Incluye un ejemplo práctico y un listado de modelos compatibles.

## Funcionalidades Clave
- **Output Estructurado**: Demuestra cómo obtener un objeto Pydantic directamente invocando al modelo.
- **Guía de Compatibilidad**: Proporciona una lista detallada de modelos de OpenAI, Anthropic, Google Gemini y Mistral que soportan nativamente el llamado a herramientas o el modo JSON.
- **Consejos Técnicos**: Explica la diferencia entre `function_calling` y `json_mode`.

## Código Fuente
```python
from pydantic import BaseModel, Field 
from langchain_google_genai import ChatGoogleGenerativeAI

class AnalisisText(BaseModel):
    resumen: str = Field(description="Resumen breve del texto.")
    sentimiento: str = Field(description="Sentimiento del texto (Positivo, nuetro o negativo)")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.6)
structured_llm = llm.with_structured_output(AnalisisText)

texto_prueba = "Me encantó la nueva película de acción, tiene muchos efectos especiales y emoción."
resultado = structured_llm.invoke(f"Analiza el siguiente texto: {texto_prueba}")

print(resultado)
```
