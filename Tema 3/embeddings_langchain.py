from langchain_google_genai import GoogleGenerativeAIEmbeddings
import numpy as np
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="llama3")
# embeddings = GoogleGenerativeAIEmbeddings(model="text-embedding-004")
# embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

texto1 = "La capital de Francia es París"
texto2 = "La casa de mi vecino es grande y esta loco por ir al parque todos los dias"

vector1 = embeddings.embed_query(texto1)
vector2 = embeddings.embed_query(texto2)

print(f"Dimension de los vectores: {len(vector1)}")

cos_sim = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))

print(f"Similitud coseno entre los vectores 1 y 2: {cos_sim:.3f}")
