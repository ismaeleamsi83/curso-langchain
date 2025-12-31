# Concepto 5: Procesamiento en Paralelo (RunnableParallel)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import PromptTemplate

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


cadena_nombre = PromptTemplate.from_template("Dime solo el nombre real del actor {entrada}")
cadena_nacionalidad = PromptTemplate.from_template("Dime solo la nacionalidad del actor {entrada}")

mapa_paralelo = RunnableParallel(
  nombre=cadena_nombre | llm,
  origen=cadena_nacionalidad | llm
)


result = mapa_paralelo.invoke({
  "entrada":"Antonio Banderas"
})

print(f"Nombre real: {result['nombre'].content}")
print(f"Nombre real: {result['origen'].content}")