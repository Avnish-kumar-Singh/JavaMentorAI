"""
LLM Tool
"""

from app.tools.base_tool import BaseTool
from app.graph.state import AgentState
from app.agents.answer_agent import AnswerAgent


class LLMTool(BaseTool):

    def __init__(self):
        self.agent = AnswerAgent()

    def execute(self, state: AgentState) -> AgentState:
        return self.agent.generate(state)