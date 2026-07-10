from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    OLLAMA_BASE_URL: str = "http://localhost:11434"
    MODEL_NAME: str = "qwen2.5:latest"
    EMBEDDING_MODEL: str = "nomic-embed-text:latest"
    CHROMA_PATH: str = "./data/chroma"
    LOG_LEVEL: str = "INFO"


settings = Settings()