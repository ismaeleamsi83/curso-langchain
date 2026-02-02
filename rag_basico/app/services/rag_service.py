from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from app.repositories.vector_repository import VectorRepository
from app.core.config import settings

class RAGService:
    """
    Este es el 'Service'. Aquí reside la lógica de negocio:
    Combinar la búsqueda en DB con la potencia del LLM.
    """
    def __init__(self):
        # 1. Instanciamos el modelo de lenguaje (Gemini)
        # Viene de la librería 'langchain_google_genai'
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=settings.GOOGLE_API_KEY,
            temperature=0  # 0 para que sea preciso, no creativo
        )
        # 2. Instanciamos nuestro repositorio (el archivo anterior)
        self.vector_repo = VectorRepository()

    async def process_question(self, query: str):
        # Obtenemos el buscador del repositorio
        retriever = self.vector_repo.get_retriever()

        # Creamos la cadena 'RetrievalQA' (Consulta con Recuperación).
        # Esta función de LangChain hace todo el flujo:
        # Busca en DB -> Crea el prompt -> Llama a Gemini -> Devuelve respuesta.
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff", # 'stuff' significa 'mete todo el contexto en el prompt'
            retriever=retriever,
            return_source_documents=True
        )

        # Ejecutamos la cadena
        response = await qa_chain.ainvoke({"query": query})
        
        return {
            "answer": response["result"],
            "sources": [{"metadata": doc.metadata} for doc in response["source_documents"]]
        }