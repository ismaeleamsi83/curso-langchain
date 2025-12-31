# Documentación: Tema 2/cv_analyzer/models/cv_model.py

Este documento describe el propósito y funcionamiento del archivo `cv_model.py`.

## Descripción General
Este archivo define la estructura de datos que el modelo de lenguaje (LLM) debe seguir al devolver el análisis de un currículum vitae. Utiliza la librería **Pydantic** para garantizar que la salida sea consistente y esté tipada.

## Funcionalidades Clave
- **BaseModel**: Emplea la clase `AnalisisCV` heredada de `BaseModel` para definir los campos esperados.
- **Fields con Descriptores**: Cada campo utiliza `Field` con una descripción detallada, lo que ayuda al LLM a entender exactamente qué información extraer o generar.
- **Validación de Datos**: Incluye validaciones básicas como `ge=0` (mayor o igual a 0) y `le=100` (menor o igual a 100) para el campo `porcentaje_ajuste`.

## Estructura del Modelo
El modelo extrae los siguientes puntos:
1. Nombre del candidato.
2. Años de experiencia.
3. Habilidades clave (lista).
4. Educación.
5. Resumen de experiencia relevante.
6. Fortalezas (lista).
7. Áreas de mejora (lista).
8. Porcentaje de ajuste al puesto.

## Código Fuente
```python
from pydantic import BaseModel, Field

class AnalisisCV(BaseModel):
    """Modelo de datos para el análisis completo de un CV."""
    
    nombre_candidato: str = Field(description="Nombre completo del candidato extraido del CV.")
    experiencia_años: int = Field(description="Años totales de experiencia laboral relevante.")
    habilidades_clave: list[str] = Field(description="Lista de las 5-7 habilidades del candidato más relevantes para el puesto.")
    education: str = Field(description="Nivel educativo más alto y especialización principal.")
    experiencia_relevante: str = Field(description="Resumen conciso de la experiencia más relevante para el puesto especifico.")
    fortalezas: list[str] = Field(description="3-5 fortalezas del candidato basadas en su perfil.")
    areas_mejora: list[str] = Field(description="2-4 áreas donde el candidato podría desarrollarse o mejorar.")
    porcentaje_ajuste: int = Field(description="Porcentaje de ajuste al puesto (0-100) basado en la experiencia, habilidades y formación.", ge=0, le=100)
```
