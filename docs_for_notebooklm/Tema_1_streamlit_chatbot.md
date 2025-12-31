# Documentación: Tema 1/streamlit_chatbot.py

Este documento describe el propósito y funcionamiento del archivo `streamlit_chatbot.py` del Tema 1.

## Descripción General
Es una implementación básica de un chatbot utilizando **Streamlit** y **LangChain** con el modelo **Google Gemini**. A diferencia de las versiones finales, esta es una versión más simplificada centrada en la integración directa de mensajes.

## Funcionalidades Clave
- **Session State**: Utiliza `st.session_state.mensajes` para persistir la conversación durante la sesión.
- **Detección de Roles**: Clasifica los mensajes como `assistant` o `user` basándose en el tipo de objeto (`AIMessage` o `HumanMessage`).
- **Invocación del Modelo**: Pasa la lista completa de mensajes al modelo `chat_model.invoke(st.session_state.mensajes)` para obtener la respuesta con contexto.

## Código Fuente
```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import streamlit as st

# COnfigurar la pagina de la app
st.set_page_config(page_title="Chatbot Básico", page_icon=":robot_face:")
st.title("Chatbot Básico con LangChain")
st.markdown("Este es un chatbot básico que utiliza LangChain + Streamlit. ¡Escribe tu mensaje abajo para comenzar!")

chat_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)

# Inicializar el historial de mensajes
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar mensajes precios en la interface
for msg in st.session_state.mensajes:
    if isinstance(msg, SystemMessage):
        # No mostrar mensajes del sistema
        continue

    role = "assistant" if isinstance(msg, AIMessage) else "user"
    with st.chat_message(role):
        st.markdown(msg.content)

# Cuadro de entrada de texto de usuario
pregunta = st.chat_input("Escribe tu mensaje: ")

if pregunta:
    # Mostrar inmediatamente el mensaje del usuario en la interface
    with st.chat_message("user"):
        st.markdown(pregunta)

    # Almacenamos el mensaje del usuario en la memoria de streamlit
    st.session_state.mensajes.append(HumanMessage(content=pregunta))
    
    # Generar la respuesta usando el modelo de lenguaje
    respuesta = chat_model.invoke(st.session_state.mensajes)

    # Mostrar la respues en la interface
    with st.chat_message("assistant"):
        st.markdown(respuesta.content)

    # Almacenamos la respuesta del chatbot en la memoria de streamlit
    st.session_state.mensajes.append(respuesta)
```
