# Concepto 2: Plantillas de Prompt y LCEL (LangChain Expression Language)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate.from_template(
  'Eres un experto en tecnología. Explicame de forma breve qué es {tema}'
)

cadena = prompt | llm

result = cadena.invoke({
  "tema": "un LLM"
})

print(result.content)