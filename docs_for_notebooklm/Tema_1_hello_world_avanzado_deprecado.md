# Documentación: Tema 1/hello_world _avanzado_deprecado.py

Este documento describe el propósito y funcionamiento del archivo `hello_world _avanzado_deprecado.py`.

## Descripción General
Este script muestra una forma antigua (ahora deprecada o menos recomendada) de crear cadenas en LangChain utilizando la clase `LLMChain`. Sirve como comparación con el enfoque moderno de LCEL.

## Funcionalidades Clave
- **LLMChain**: Utiliza la clase tradicional `LLMChain` para unir un modelo de lenguaje y una plantilla de prompt.
- **Google Gemini**: Al igual que el ejemplo actual, utiliza `ChatGoogleGenerativeAI`.
- **Método .run()**: Emplea el método `.run()` (en lugar de `.invoke()`) para ejecutar la cadena directamente con el valor de la variable.

## Código Fuente
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

chat = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

plantilla = PromptTemplate(
    input_variables=["nombre"],
    template="Saluda al usuario con su nombre. \nombre del usuario: {nombre}\nAsistente:"
)

chain = LLMChain(llm=chat, prompt=plantilla)

resultado = chain.run(nombre="Isma")
print(resultado)
```
