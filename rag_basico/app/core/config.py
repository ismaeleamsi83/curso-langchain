from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Definimos las variables que esperamos. 
    # Pydantic las buscará automáticamente en el archivo .env o en el sistema.
    GOOGLE_API_KEY: str
    DATABASE_URL: str

    # Configuración de Pydantic para que lea el archivo .env
    model_config = SettingsConfigDict(env_file=".env")

# Instanciamos para que otros archivos hagan: from config import settings
settings = Settings()
