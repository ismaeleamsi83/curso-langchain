from langchain_community.vectorstores import Chroma
# from langchain_ollama import OllamaEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# embeddings = OllamaEmbeddings(model="llama3")
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

loader = PyPDFDirectoryLoader("contratos")
documentos = loader.load()

print(f"Se cargaron {len(documentos)} documentos desde el directorio.")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs_split = text_splitter.split_documents(documentos)

print(f"Se crearon {len(docs_split)} chunks de texto.")

vector_store = Chroma.from_documents(
    docs_split, 
    embeddings,
    persist_directory="chroma_db"
)

# consulta = "¿Cuál es el inmueble que forma parte del contrato en el que participa Maria Jimenez Campos?"
consulta = "¿Donde se encuentra el local del contrato en el que participa Maria Jimenez Campos?"

resultados = vector_store.similarity_search(consulta, k=2)

print("Top 3 documentos más similares a la consulta\n")
for i, doc in enumerate(resultados, start=1):
    print(f"Contenido: {doc.page_content}\n")
    print(f"Metadata: {doc.metadata}\n")

