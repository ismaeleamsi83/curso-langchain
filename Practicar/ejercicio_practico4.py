# Concepto 4: Salidas Estructuradas con Pydantic

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Actor(BaseModel):
  nombre:str = Field(description="El nombre completo del actor.")
  pelicula_famosa:list[str] = Field(description="Es la película más icónica del actor.")

llm_estructurado = llm.with_structured_output(Actor)

prompt = ChatPromptTemplate([
  ("system", "Eres un profesional en actores de Hollywood"),
  ("human", "Que existos ha tenido {actor}")
])

cadena = prompt | llm_estructurado

result = cadena.invoke({
  "actor": "Antonio Banderas"
})

print(result)