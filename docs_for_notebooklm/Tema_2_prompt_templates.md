# Documentación: Tema 2/prompt_templates.py

Este documento describe el propósito y funcionamiento del archivo `prompt_templates.py`.

## Descripción General
Este es un ejemplo básico que introduce el concepto de `PromptTemplate` en LangChain, mostrando cómo crear plantillas reutilizables con variables dinámicas.

## Funcionalidades Clave
- **Template Reutilizable**: Define un string con marcadores de posición (por ejemplo, `{producto}`).
- **Método .format()**: Permite inyectar valores reales en la plantilla de forma programática.

## Código Fuente
```python
from langchain_core.prompts import PromptTemplate

template = "Eres un experto en marketing. Sugiere un eslogan creativo para un producto {producto}"

prompt = PromptTemplate(
    template = template,
    input_variables = ["producto"]
)

prompt_lleno = prompt.format(producto="café orgánico")
print(prompt_lleno)
```
