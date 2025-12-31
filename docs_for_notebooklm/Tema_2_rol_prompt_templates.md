# Documentación: Tema 2/rol_prompt_templates.py

Este documento describe el propósito y funcionamiento del archivo `rol_prompt_templates.py`.

## Descripción General
Este script profundiza en el uso de plantillas de chat, demostrando cómo parametrizar no solo el mensaje del usuario, sino también el comportamiento del sistema (rol, especialidad, tono).

## Funcionalidades Clave
- **SystemMessagePromptTemplate**: Permite definir plantillas específicas para el mensaje de sistema.
- **HumanMessagePromptTemplate**: Permite definir plantillas específicas para el mensaje del usuario.
- **Multi-parametrización**: El prompt final depende de 5 variables diferentes, lo que permite una personalización extrema del asistente.

## Código Fuente
```python
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

plantilla_sistema = SystemMessagePromptTemplate.from_template("" \
    "Eres un {rol} especializado en {especialidad}. Responde de manera {tono}"
)

plantilla_humano = HumanMessagePromptTemplate.from_template("" \
    "Mi pregunta sobre {tema} es: {pregunta}"
)

chat_prompt = ChatPromptTemplate.from_messages([
    plantilla_sistema,
    plantilla_humano
])

mensajes = chat_prompt.format_messages(
    rol="nutricionista",
    especialidad="dietas veganas",
    tono="profesional pero accesible",
    tema="proteinas vegetales",
    pregunta="¿Cuales son las mejores fuentes de proteína vegana para un atleta profesional?"
)

for m in mensajes:
    print(m.content)
```
