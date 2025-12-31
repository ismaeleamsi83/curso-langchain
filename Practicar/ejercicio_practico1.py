# Concepto 1: La Invocación Directa y el Acceso al Contenido

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

result = llm.invoke("¿Qué es un LLM?")

print(result.content)
