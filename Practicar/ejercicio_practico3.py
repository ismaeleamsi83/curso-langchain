# Concepto 3: Roles de Mensajes (System y Human)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = ChatPromptTemplate([
  ("system", "Eres un asistente experto en {especialidad}. Responde de forma {tono}."),
  ("human", "Explícame qué es {concepto}.") 
])

cadena = prompt | llm 

result = cadena.invoke({
  "especialidad": "historiador",
  "tono": "sarcastico",
  "concepto": "la civilización milenaria"
})

print(result.content)
