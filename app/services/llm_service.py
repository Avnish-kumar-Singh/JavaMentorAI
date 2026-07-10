"""
LLM Service

Responsible for communicating with the local Ollama model.
"""

from langchain_ollama import ChatOllama

from app.config.settings import settings
from app.config.logging_config import logger


class LLMService:
    """
    Handles communication with the LLM.
    """

    def __init__(self):
        logger.info("Initializing Ollama model...")

        self.llm = ChatOllama(
            model=settings.MODEL_NAME,
            base_url=settings.OLLAMA_BASE_URL,
            temperature=0.2,
        )

        logger.info(f"Model Loaded: {settings.MODEL_NAME}")

    def invoke(self, prompt: str) -> str:
        """
        Send a prompt to the LLM and return the response.
        """

        logger.info("Sending prompt to LLM...")

        response = self.llm.invoke(prompt)

        logger.info("Received response from LLM.")

        return response.content