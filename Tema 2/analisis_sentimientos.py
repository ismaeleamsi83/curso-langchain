from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_google_genai import GoogleGenerativeAI
import json

# Configuración de Google Generative AI
llm = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# Preprocesador de Texto
def preprocess_text(text):
    return text.strip()[:500]

preprocessor = RunnableLambda(preprocess_text)

# Generador de Resúmenes
def generate_summary(text):
    prompt = f"Resume en una sola oración: {text}"
    response = llm.invoke(prompt)
    return response

summary_branch = RunnableLambda(generate_summary)

# Analizador de Sentimientos
def analyze_sentiment(text):
    prompt = f"""Analiza el sentimiento del siguiente texto.
    Responde ÚNICAMENTE en formato JSON válido:
    {{"sentimiento": "positivo|negativo|neutro", "razon": "justificacion breve"}} 
    Texto: {text}"""

    response = llm.invoke(prompt)

    # DEBUG: Ver qué está devolviendo el LLM
    print(f"DEBUG - Respuesta del LLM: {repr(response)}")

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return {"sentimiento": "neutro", "razon": "Error en análisis"}

sentiment_branch = RunnableLambda(analyze_sentiment)

# Función de Combinación
def merge_results(data):
    """Combina los resultados de ambas ramas en un formato unificado"""
    return {
        "resumen": data["resumen"],
        "sentimiento": data["sentimiento_data"]["sentimiento"],
        "razon": data["sentimiento_data"]["razon"]
    }

merger = RunnableLambda(merge_results)

parallel_analysis = RunnableParallel({
    "resumen": summary_branch, 
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