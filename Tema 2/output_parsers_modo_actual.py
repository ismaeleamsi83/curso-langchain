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
print(resultado.model_dump_json())














# listado_modelos_structured_output.py

"""
LISTADO DE COMPATIBILIDAD: .with_structured_output()
--------------------------------------------------
Esta funcionalidad permite que el modelo devuelva objetos validados (Pydantic) 
o diccionarios JSON en lugar de texto plano. Requiere que el modelo soporte 
nativamente 'Tool Calling' o 'JSON Mode'.
"""

# =============================================================================
# 1. MODELOS QUE SÍ SOPORTAN (Nativamente a través de LangChain)
# =============================================================================

SOPORTADOS = [
    # --- OpenAI ---
    "gpt-4o",                # Recomendado: El más robusto en output estructurado.
    "gpt-4o-mini",           # Excelente relación calidad/precio para JSON.
    "gpt-4-turbo",           # Soporta tanto Tool Calling como JSON Mode.
    "gpt-4",                 # Soporta Tool Calling.
    "gpt-3.5-turbo",         # Soporta Tool Calling.

    # --- Anthropic (Claude) ---
    "claude-3-5-sonnet-latest", # El más preciso de Anthropic para esta tarea.
    "claude-3-opus-20240229",   # Soporta Tool Calling nativo.
    "claude-3-sonnet-20240229",
    "claude-3-haiku-20240307",

    # --- Google Gemini ---
    "gemini-1.5-pro",        # Soporta output estructurado vía VertexAI o GenerativeAI.
    "gemini-1.5-flash",      # Rápido y eficiente para esquemas sencillos.
    "gemini-1.0-pro",

    # --- Mistral ---
    "mistral-large-latest",  # Soporta Tool Calling nativo.
    "mistral-small-latest",
    "codestral-latest",

    # --- Groq (Modelos específicos con Tool Calling) ---
    "llama3-70b-8192",       # A través de la implementación de Groq.
    "llama3-8b-8192",
    "mixtral-8x7b-32768",

    # --- FireWorks AI / Together AI ---
    # La mayoría de modelos Llama 3 (70b/8b) y Qwen en estos providers 
    # que han sido ajustados para Tool Calling.
]

# =============================================================================
# 2. MODELOS QUE NO SOPORTAN (O requieren wrappers/técnicas manuales)
# =============================================================================

NO_SOPORTADOS_NATIVAMENTE = [
    # --- Modelos Legacy ---
    "gpt-3.5-turbo-instruct", # Solo soporta completado de texto, no tools.
    "text-davinci-003",       # Obsoleto.
    
    # --- Anthropic Legacy ---
    "claude-2.1",             # No tiene soporte nativo para with_structured_output (usa XML).
    "claude-instant-1.2",

    # --- Modelos Locales Pequeños (vía Ollama/Llama-cpp) ---
    # Muchos modelos de menos de 7B parámetros fallan al seguir esquemas JSON complejos.
    "phi-3-mini",             # Demasiado pequeño para lógica de herramientas compleja.
    "tinyllama",              # Incapaz de mantener la estructura JSON.

    # --- Otros ---
    "granite-models",         # Depende de la versión, pero el soporte es inconsistente.
]

# =============================================================================
# NOTAS TÉCNICAS:
# 1. Requisito: Para usar .with_structured_output(), debes tener instalada 
#    la librería del partner (ej: langchain-openai, langchain-anthropic).
# 2. Métodos: LangChain suele usar dos métodos bajo el capó:
#    - 'function_calling': El modelo usa su lógica interna de herramientas.
#    - 'json_mode': El modelo es forzado a escribir un string JSON.
# =============================================================================

def check_support(model_name):
    if model_name in SOPORTADOS:
        return f"✅ El modelo '{model_name}' es compatible."
    return f"❌ El modelo '{model_name}' NO es compatible o no está verificado."