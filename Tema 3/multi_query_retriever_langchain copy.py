from langchain_community.vectorstores import Chroma
# from langchain_ollama import OllamaEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_google_genai import GoogleGenerativeAI

# embeddings = OllamaEmbeddings(model="llama3")
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

llm = GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

vectorstore = Chroma(
    embedding_function=embeddings,
    persist_directory="chroma_db"
)

base_retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 2})
retriever = MultiQueryRetriever.from_llm(retriever=base_retriever, llm=llm)

consulta = "¿Donde se encuentra el local del contrato en el que participa Maria Jimenez Campos?"
resultados = retriever.invoke(consulta)

print("Top 2 documentos más similares a la consulta\n")
for i, doc in enumerate(resultados, start=1):
    print(f"Contenido: {doc.page_content}\n")
    print(f"Metadata: {doc.metadata}\n")

