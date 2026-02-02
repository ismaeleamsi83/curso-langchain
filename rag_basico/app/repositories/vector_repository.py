from langchain_community.vectorstores import PGVector
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.core.config import settings

class VectorRepository:
    """
    Esta clase es un 'Repository'. Su única responsabilidad es 
    gestionar cómo se guardan y recuperan los vectores en Postgres.
    """
    def __init__(self):
        # 1. Obtenemos el modelo de 'Embeddings' de Google.
        # Sirve para convertir texto en números (vectores).
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=settings.GOOGLE_API_KEY
        )
        # 2. Configuramos la conexión a PGVector (extensión de Postgres)
        self.connection_string = settings.DATABASE_URL
        self.collection_name = "aviacion_chunks"

    def get_retriever(self):
        # Esta función crea un 'retriever' (un buscador).
        # Saca la lógica de 'LangChain Community' para conectar con SQL.
        vector_store = PGVector(
            connection_string=self.connection_string,
            embedding_function=self.embeddings,
            collection_name=self.collection_name
        )
        # Devolvemos el buscador configurado para traer los 3 documentos más parecidos
        return vector_store.as_retriever(search_kwargs={"k": 3})