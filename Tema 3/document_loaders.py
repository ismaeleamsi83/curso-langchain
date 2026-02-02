from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader


# PyPDFLoader
loader = PyPDFLoader("Ismael-Rey-Plata-CV.pdf")

pages = loader.load()

for i, page in enumerate(pages):
    print(f"=== Página {i+1} ===")
    print(f"Contenido: {page.page_content}")
    print(f"Metadatos: {page.metadata}")
    print("\n")

# print(dir(pages[0]))
# print(pages)



# WebBaseLoader
loaderWeb = WebBaseLoader("https://es.wikipedia.org/wiki/Inteligencia_artificial")

pagesWeb = loaderWeb.load()

for i, page in enumerate(pagesWeb):
    print(f"=== Página {i+1} ===")
    print(f"Contenido: {page.page_content}")
    print(f"Metadatos: {page.metadata}")
    print("\n")
