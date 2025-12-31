# Documentación: Descargas/streamlit_chatbot_final.py

Este documento describe el propósito y funcionamiento del archivo `streamlit_chatbot_final.py`.

## Descripción General
Este archivo implementa un chatbot interactivo utilizando la librería **Streamlit** para la interfaz de usuario y **LangChain** para la lógica del modelo de lenguaje. Utiliza modelos de OpenAI (como GPT-3.5 o GPT-4) y permite al usuario configurar la temperatura y el modelo desde la barra lateral.

## Funcionalidades Clave
- **Interfaz de Chat**: Implementa una interfaz de chat moderna con `st.chat_message` y `st.chat_input`.
- **Configuración Dinámica**: Permite ajustar la `temperatura` y el `modelo` en tiempo real.
- **Memoria de Conversación**: Utiliza `st.session_state` para mantener el historial de la conversación.
- **LCEL (LangChain Expression Language)**: Define la cadena de procesamiento usando la sintaxis de tubería (`|`).
- **Streaming**: La respuesta del bot se muestra en tiempo real mediante el método `.stream()`.

## Código Fuente
```python
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate

# Configuración inicial
st.set_page_config(page_title="Chatbot Básico", page_icon="🤖")
st.title("🤖 Chatbot Básico con LangChain")
st.markdown("Este es un *chatbot de ejemplo* construido con LangChain + Streamlit. ¡Escribe tu mensaje abajo para comenzar!")

with st.sidebar:
    st.header("Configuración")
    temperature = st.slider("Temperatura", 0.0, 1.0, 0.5, 0.1)
    model_name = st.selectbox("Modelo", ["gpt-3.5-turbo", "gpt-4", "gpt-4o-mini"])
    
    # Recrear el modelo con nuevos parámetros
    chat_model = ChatOpenAI(model=model_name, temperature=temperature)

# Inicializar el historial de mensajes en session_state
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Crear el template de prompt con comportamiento específico
prompt_template = PromptTemplate(
    input_variables=["mensaje", "historial"],
    template="""Eres un asistente útil y amigable llamado ChatBot Pro. 

Historial de conversación:
{historial}

Responde de manera clara y concisa a la siguiente pregunta: {mensaje}"""
)

# Crear cadena usando LCEL (LangChain Expression Language)
cadena = prompt_template | chat_model

# Renderizar historial existente
for msg in st.session_state.mensajes:
    if isinstance(msg, SystemMessage):
        continue  # no mostrar mensajes del sistema al usuario
    
    role = "assistant" if isinstance(msg, AIMessage) else "user"
    with st.chat_message(role):
        st.markdown(msg.content)

if st.button("🗑️ Nueva conversación"):
    st.session_state.mensajes = []
    st.rerun()

# Input de usuario
pregunta = st.chat_input("Escribe tu mensaje:")

if pregunta:
    # Mostrar y almacenar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(pregunta)
    
    # Generar y mostrar respuesta del asistente
    try:
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""

            # Streaming de la respuesta
            for chunk in cadena.stream({"mensaje": pregunta, "historial": st.session_state.mensajes}):
                full_response += chunk.content
                response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
        
        st.session_state.mensajes.append(HumanMessage(content=pregunta))
        st.session_state.mensajes.append(AIMessage(content=full_response))
        
    except Exception as e:
        st.error(f"Error al generar respuesta: {str(e)}")
        st.info("Verifica que tu API Key de OpenAI esté configurada correctamente.")
```
