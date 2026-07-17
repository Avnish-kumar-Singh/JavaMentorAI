# """
# Retriever

# Retrieves the most relevant chunks from ChromaDB.
# """

# from app.rag.vector_store import VectorStore
# from app.config.logging_config import logger


# class Retriever:

#     def __init__(self):

#         self.vector_store = VectorStore()

#         self.retriever = self.vector_store.get_vector_store().as_retriever(
#             search_kwargs={"k": 3}
#         )

#     def retrieve(self, query: str):

#         logger.info("Searching relevant documents...")

#         docs = self.retriever.invoke(query)

#         logger.info(f"Retrieved {len(docs)} document(s).")

#         return docs






"""
Retriever

Retrieves the most relevant chunks from ChromaDB.
"""

from app.rag.vector_store import VectorStore
from app.config.logging_config import logger


class Retriever:

    def __init__(self):

        self.vector_store = VectorStore()

        self.retriever = self.vector_store.get_vector_store().as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 4,
                "fetch_k": 10,
                "lambda_mult": 0.7,
            },
        )

    def retrieve(self, query: str):

        logger.info("Searching relevant documents...")

        docs = self.retriever.invoke(query)

        logger.info(f"Retrieved {len(docs)} document(s).")

        return docs