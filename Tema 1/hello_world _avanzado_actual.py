from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

chat = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# plantilla
plantilla = PromptTemplate(
    input_variables=["nombre"],
    template="Saluda al usuario con su nombre. \nombre del usuario: {nombre}\nAsistente:"
)

# cadena de procesamiento
chain = plantilla | chat

# invocar la cadena de procesamiento
resultado = chain.invoke({"nombre": "Isma"})
print(resultado.content)

# LCEL LangChain Expression Language