# Concepto 6: Funciones Personalizadas (RunnableLambda)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate.from_template(
  "Háblame brevemente sobre {tema}"
)

def limpiar_texto(texto):
  return {"tema": texto["tema"].strip().upper()}

cadena = RunnableLambda(limpiar_texto) | prompt | llm

result = cadena.invoke(
  {"tema": "iracing  "}
)

print(result.content)

