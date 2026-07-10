"""
LLM Service
"""

from langchain_ollama import ChatOllama

from app.config.settings import settings
from app.config.logging_config import logger


class LLMService:

    def __init__(self):

        logger.info("Initializing Ollama model...")

        self.llm = ChatOllama(
            model=settings.MODEL_NAME,
            base_url=settings.OLLAMA_BASE_URL,
            temperature=0.2,
        )

        logger.info(f"Model Loaded: {settings.MODEL_NAME}")

    def invoke(self, prompt: str) -> str:

        logger.info("Sending prompt to LLM...")

        try:

            response = self.llm.invoke(prompt)

            logger.info("Received response from LLM.")

            return response.content

        except Exception as e:

            logger.exception("LLM Error")

            return f"Error: {str(e)}"