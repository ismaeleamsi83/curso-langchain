from langchain_community.vectorstores import Chroma
# from langchain_ollama import OllamaEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# embeddings = OllamaEmbeddings(model="llama3")
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")


vectorstore = Chroma(
    embedding_function=embeddings,
    persist_directory="chroma_db"
)

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 2})

consulta = "¿Donde se encuentra el local del contrato en el que participa Maria Jimenez Campos?"

resultados = retriever.invoke(consulta)

print("Top 2 documentos más similares a la consulta\n")
for i, doc in enumerate(resultados, start=1):
    print(f"Contenido: {doc.page_content}\n")
    print(f"Metadata: {doc.metadata}\n")

