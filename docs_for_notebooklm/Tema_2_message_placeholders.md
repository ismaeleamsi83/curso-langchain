# Documentación: Tema 2/message_placeholders.py

Este documento describe el propósito y funcionamiento del archivo `message_placeholders.py`.

## Descripción General
Este script enseña cómo manejar el historial de una conversación utilizando `MessagesPlaceholder`. Es una técnica esencial para crear chatbots que mantengan el contexto.

## Funcionalidades Clave
- **MessagesPlaceholder**: Actúa como un contenedor dinámico donde se inyectará una lista de objetos de mensaje (`HumanMessage`, `AIMessage`).
- **format_messages**: Permite pasar el historial completo como una variable, facilitando que el modelo reciba toda la conversación previa antes de la pregunta actual.

## Código Fuente
```python
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente útil que mantiene el contexto de la conversación."),
    MessagesPlaceholder(variable_name="historial"),
    ("human", "Usuario: {pregunta_actual}")
])

# Simulamos un historial de conversación
historial_conversacion = [
    HumanMessage(content="Usuario: ¿Cuál es la capital de Francia?"),
    AIMessage(content="IA: La capital de Francia es París."),
    HumanMessage(content="Usuario: ¿Y cuántos habitantes tiene?"),
    AIMessage(content="IA: París tiene aproximadamente 2.2 millones de habitantes en la ciudad propiamente dicha.")
]

mensajes = chat_prompt.format_messages(
    historial=historial_conversacion,
    pregunta_actual="¿Puedes decirme algo interesante de su arquitectura?"
)

for m in mensajes:
    print(m.content)
```
