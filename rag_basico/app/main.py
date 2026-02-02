from fastapi import FastAPI
from app.api.v1 import chat

# Creamos la aplicación principal
app = FastAPI(
    title="Profesional RAG API",
    description="API con FastAPI, LangChain y Google Gemini"
)

# Registramos las rutas que creamos en el archivo anterior
app.include_router(chat.router, prefix="/api/v1", tags=["Chat con IA"])

@app.get("/")
def health_check():
    return {"status": "online", "message": "API de RAG funcionando"}