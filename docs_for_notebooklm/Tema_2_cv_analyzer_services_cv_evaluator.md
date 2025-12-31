# Documentación: Tema 2/cv_analyzer/services/cv_evaluator.py

Este documento describe el propósito y funcionamiento del archivo `cv_evaluator.py`.

## Descripción General
Este servicio es el corazón lógico de la aplicación. Se encarga de orquestar la llamada al modelo de lenguaje (Gemini), aplicando la estructura de salida (modelo Pydantic) y los prompts definidos anteriormente.

## Funcionalidades Clave
- **Output Estructurado**: Utiliza `.with_structured_output(AnalisisCV)` para forzar al modelo a devolver datos válidos según el esquema definido.
- **Manejo de Errores**: Implementa un bloque `try/except` que devuelve un objeto `AnalisisCV` con valores por defecto en caso de fallo, evitando que la aplicación se detenga.
- **Configuración del LLM**: Configura el modelo con una temperatura baja (`0.2`) para favorecer respuestas objetivas y precisas.

## Código Fuente
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from models.cv_model import AnalisisCV
from prompts.cv_prompts import crear_sistema_prompts

def crear_evaluador_cv():
    modelo_base = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2
    )

    modelo_estructurado = modelo_base.with_structured_output(AnalisisCV)
    chat_prompt = crear_sistema_prompts()
    cadena_evaluacion = chat_prompt | modelo_estructurado

    return cadena_evaluacion


def evaluar_candidato(texto_cv: str, descripcion_puesto: str) -> AnalisisCV:
    try:
        cadena_evaluacion = crear_evaluador_cv()
        resultado = cadena_evaluacion.invoke({
            "texto_cv": texto_cv,
            "descripcion_puesto": descripcion_puesto
        })

        return resultado
    except Exception as e:
        return AnalisisCV(
            nombre_candidato="Error en procesamiento",
            experiencia_años = 0,
            habilidades_clave=["Error al procesar CV"],
            education="No se puede determinar",
            experiencia_relevante="Error durante el análisis",
            fortalezas=["Requiere revision manual del CV"],
            areas_mejora=["Verificar formato y legibilidad del PDF"],
            porcentaje_ajuste=0,
        )
```
