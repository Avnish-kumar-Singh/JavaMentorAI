"""
RAG Tool
"""

from app.tools.base_tool import BaseTool
from app.graph.state import AgentState
from app.rag.retriever import Retriever
from app.agents.answer_agent import AnswerAgent
from app.synthesis.context_builder import ContextBuilder
from app.config.logging_config import logger


class RAGTool(BaseTool):

    def __init__(self):

        self.retriever = Retriever()
        self.answer_agent = AnswerAgent()
        self.context_builder = ContextBuilder()

    def execute(self, state: AgentState) -> AgentState:

        logger.info("RAG Tool Started")

        # Retrieve relevant documents
        documents = self.retriever.retrieve(
            state["user_query"]
        )

        # Build clean context
        context = self.context_builder.build(documents)

        # ---------- DEBUG (Remove later) ----------
        # print("\n")
        # print("=" * 80)
        # print("RETRIEVED CONTEXT")
        # print("=" * 80)
        # print(context)
        # print("=" * 80)
        # print("\n")
        # ------------------------------------------

        state["context"] = context

        logger.info("Passing context to Answer Agent")

        result = self.answer_agent.generate(state)

        logger.info("RAG Tool Finished")

        return result