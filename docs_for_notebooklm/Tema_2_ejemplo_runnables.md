# Documentación: Tema 2/ejemplo_runnables.py

Este documento describe el propósito y funcionamiento del archivo `ejemplo_runnables.py`.

## Descripción General
Este es un ejemplo educativo minimalista que demuestra el uso de `RunnableLambda` y la composición de cadenas mediante el operador pipe (`|`).

## Funcionalidades Clave
- **RunnableLambda**: Convierte funciones lambda de Python y funciones estándar en componentes de LangChain que pueden ser encadenados.
- **Composición**: Muestra cómo una salida (en este caso un string) se convierte en la entrada del siguiente paso (`duplicar_text`).

## Código Fuente
```python
from langchain_core.runnables import RunnableLambda

paso1 = RunnableLambda( lambda x: f"Numero {x}")

def duplicar_text(texto):
    return [texto] * 2

paso2 = RunnableLambda(duplicar_text)

cadena = paso1 | paso2

resultado = cadena.invoke(43)

print(resultado)
```
