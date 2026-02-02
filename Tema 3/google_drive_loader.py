from langchain_community.document_loaders import GoogleDriveLoader

credentials_path = "credentials.json"
token_path = "token.json"

loader = GoogleDriveLoader(
    folder_id="1b34ZHjCJc88Y4okwUJaxh1fQWLY7sIkl",
    credentials_path=credentials_path,
    token_path=token_path,
)

documents = loader.load()

print(f"Metadatos: {documents[0].metadata}")
print(f"Contenido: {documents[0].page_content}")

# Mira en la carpeta contratos del curso langchain