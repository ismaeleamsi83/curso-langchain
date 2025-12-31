# Documentación: Tema 1/hello_world _avanzado_actual.py

Este documento describe el propósito y funcionamiento del archivo `hello_world _avanzado_actual.py`.

## Descripción General
Este script es un ejemplo de "Hola Mundo" avanzado utilizando **LangChain** y el modelo **Google Gemini**. Muestra la forma moderna (actual) de definir cadenas de procesamiento utilizando **LCEL (LangChain Expression Language)**.

## Funcionalidades Clave
- **Integración con Google Gemini**: Utiliza `ChatGoogleGenerativeAI` para interactuar con el modelo `gemini-2.5-flash`.
- **Plantillas de Prompt**: Emplea `PromptTemplate` para estructurar la entrada al modelo.
- **Uso de LCEL**: Implementa la cadena de procesamiento usando el operador pipe (`|`), lo que facilita la composición de componentes.
- **Invocación**: Utiliza el método `.invoke()` para ejecutar la cadena con un diccionario de parámetros.

## Código Fuente
```python
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
```
