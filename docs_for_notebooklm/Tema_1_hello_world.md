# Documentación: Tema 1/hello_world.py

Este documento describe el propósito y funcionamiento del archivo `hello_world.py`.

## Descripción General
Este es el ejemplo más básico de uso de LangChain con Google Gemini. Se centra en realizar una sola pregunta al modelo sin usar plantillas de prompt ni cadenas complejas.

## Funcionalidades Clave
- **Conexión Directa**: Invoca directamente al modelo `ChatGoogleGenerativeAI`.
- **Invocación Simple**: Utiliza el método `.invoke()` pasando un string simple como pregunta.
- **Acceso al Contenido**: Muestra cómo acceder a la respuesta a través del atributo `.content`.

## Código Fuente
```python
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

pregunta = "¿En qué año llegó el ser humano a la luna por primera vez?"
print("Pregunta: ", pregunta)

respuesta = llm.invoke(pregunta)
print("Respuesta del modelo: ", respuesta.content)
```
