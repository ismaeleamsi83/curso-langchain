# Documentación: Tema 2/chat_prompt_template.py

Este documento describe el propósito y funcionamiento del archivo `chat_prompt_template.py`.

## Descripción General
Este script introduce el uso de `ChatPromptTemplate` de LangChain. Es un ejemplo fundamental de cómo estructurar conversaciones entre diferentes roles (sistema y humano) de manera programática.

## Funcionalidades Clave
- **Definición de Roles**: Utiliza tuplas `("system", "human")` para definir la estructura del mensaje.
- **Formateo de Mensajes**: Emplea `.format_messages()` para inyectar variables en el template y generar una lista de objetos de mensaje listos para ser enviados a un modelo de chat.

## Código Fuente
```python
from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un traductor del español al inglés muy preciso."),
    ("human", "{texto}")
])

mensajes = chat_prompt.format_messages(texto="Hola mundo, como estas?")

for m in mensajes:
    print(f"{type(m)}: {m.content}")
```
