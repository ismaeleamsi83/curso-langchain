from fastapi import APIRouter, Depends
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.rag_service import RAGService

# Creamos un router, que es como una 'sub-sección' de URLs
router = APIRouter()

# Definimos el endpoint POST
# 'response_model' asegura que devolvamos lo que prometimos en el Schema
@router.post("/ask", response_model=ChatResponse)
async def ask_question(
    request: ChatRequest, 
    # Usamos Inyección de Dependencias (Depends). 
    # FastAPI crea una instancia de RAGService automáticamente cuando se llama al endpoint.
    service: RAGService = Depends()
):
    # Llamamos a la lógica de negocio en el servicio
    result = await service.process_question(request.question)
    return result