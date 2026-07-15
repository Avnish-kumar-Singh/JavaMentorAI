"""
RAG Tool
"""

from app.tools.base_tool import BaseTool
from app.graph.state import AgentState
from app.rag.retriever import Retriever
from app.agents.answer_agent import AnswerAgent


class RAGTool(BaseTool):

    def __init__(self):

        self.retriever = Retriever()
        self.answer_agent = AnswerAgent()

    def execute(self, state: AgentState) -> AgentState:

        documents = self.retriever.retrieve(
            state["user_query"]
        )

        context = "\n\n".join(
            doc.page_content for doc in documents
        )

        state["context"] = context

        return self.answer_agent.generate(state)