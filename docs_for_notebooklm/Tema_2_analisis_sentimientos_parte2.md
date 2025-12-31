# Documentación: Tema 2/analisis_sentimientos_parte2.py

Este documento describe el propósito y funcionamiento del archivo `analisis_sentimientos_parte2.py`.

## Descripción General
Este script es la continuación de la serie de análisis de sentimientos, utilizando el modelo de **Google Gemini**. Implementa un flujo de trabajo que incluye preprocesamiento, resumen y análisis de sentimientos en paralelo, culminando con la combinación de resultados.

## Funcionalidades Clave
- **Google Gemini Integration**: Utiliza `GoogleGenerativeAI` con el modelo `gemini-2.5-flash`.
- **RunnableParallel**: Orquestación de ramas paralelas para el procesamiento eficiente de tareas independientes.
- **Batch Processing**: Demuestra cómo manejar múltiples entradas simultáneamente usando `chain.batch()`.

## Código Fuente
```python
from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_google_genai import GoogleGenerativeAI
import json

# Configuración del modelo
llm = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# Preprocesador: limpia espacios y limita a 500 caracteres
def preprocess_text(text):
    """Limpia el texto eliminando espacios extras y limitando longitud"""
    return text.strip()[:500]

preprocessor = RunnableLambda(preprocess_text)

# Generación de resumen
def generate_summary(text):
    """Genera un resumen conciso del texto"""
    prompt = f"Resume en una sola oración: {text}"
    response = llm.invoke(prompt)
    return response

summary_brach = RunnableLambda(generate_summary)

# Análisis de sentimiento con formato JSON
def analyze_sentiment(text):
    """Analiza el sentimiento y devuelve resultado estructurado"""
    prompt = f"""Analiza el sentimiento del siguiente texto.
    Responde ÚNICAMENTE en formato JSON válido:
    {{"sentimiento": "positivo|negativo|neutro", "razon": "justificación breve"}}
    
    Texto: {text}"""
    
    response = llm.invoke(prompt)
    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {"sentimiento": "neutro", "razon": "Error en análisis"}
    
sentiment_branch = RunnableLambda(analyze_sentiment)

# Combinación de resultados
def merge_results(data):
    """Combina los resultados de ambas ramas en un formato unificado"""
    return {
        "resumen": data["resumen"],
        "sentimiento": data["sentimiento_data"]["sentimiento"],
        "razon": data["sentimiento_data"]["razon"]
    }

merger = RunnableLambda(merge_results)

parallel_analysis = RunnableParallel({
    "resumen": summary_brach,
    "sentimiento_data": sentiment_branch
})

# Cadena completa
chain = preprocessor | parallel_analysis | merger

reviews_batch = [
    "Excelente producto, muy satisfecho con la compra",
    "Terrible calidad, no lo recomiendo para nada",
    "Está bien, cumple su función básica pero nada especial"
]

resultado_batch = chain.batch(reviews_batch)

print(resultado_batch)
```
