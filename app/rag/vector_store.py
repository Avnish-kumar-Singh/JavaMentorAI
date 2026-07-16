# """
# Vector Store

# Stores embeddings in ChromaDB.
# """

# from langchain_chroma import Chroma

# from app.rag.embeddings import EmbeddingGenerator
# from app.config.logging_config import logger


# class VectorStore:

#     def __init__(self):

#         self.embedding_model = EmbeddingGenerator()

#         self.db = Chroma(
#             persist_directory="data/chroma_db",
#             embedding_function=self.embedding_model.embeddings,
#         )

#     def add_documents(self, documents):

#         logger.info("Adding documents to ChromaDB...")

#         self.db.add_documents(documents)

#         logger.info("Documents stored successfully.")

#     def get_vector_store(self):

#         return self.db





"""
Vector Store

Stores embeddings in ChromaDB.
"""

from langchain_chroma import Chroma

from app.rag.embeddings import EmbeddingGenerator
from app.config.logging_config import logger


class VectorStore:

    def __init__(self):

        self.embedding_model = EmbeddingGenerator()

        self.db = Chroma(
            persist_directory="data/chroma_db",
            embedding_function=self.embedding_model.embeddings,
        )

    def add_documents(self, documents):

        logger.info("Adding documents to ChromaDB...")

        self.db.add_documents(documents)

        logger.info("Documents stored successfully.")

    def get_vector_store(self):

        return self.db

    def document_exists(self, source: str) -> bool:
        """
        Check whether a document from this source
        has already been indexed.
        """

        results = self.db.get(
            where={"source": source}
        )

        return len(results["ids"]) > 0