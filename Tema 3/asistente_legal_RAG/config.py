# Configuracion de los modelos
EMBEDDING_MODEL = "gemini-embedding-001"
QUERY_MODEL = "gemini-2.5-flash" # Modelo para generar consultas puede ser modelo mas pequeño
GENERATION_MODEL = "gemini-2.5-flash" # Modelo para generar respuestas puede ser modelo mas grande

# Configuracion de la base de datos
CHROMA_DB_PATH = "..\\chroma_db"

# Configuracion del retriever
SEARCH_TYPE = "mmr" # Puede ser "mmr" o "similarity"
MMR_DIVERSITY_LAMBDA = 0.7
MMR_FETCH_K = 20
SEARCH_K = 2

# Configuracion alternativa para retriever hibrido
ENABLE_HYBRID_SEARCH = True
SIMILARITY_THRESHOLD = 0.75