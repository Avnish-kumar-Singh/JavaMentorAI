"""
LLM Tool
"""

from app.graph.state import AgentState
from app.agents.answer_agent import AnswerAgent


class LLMTool:

    def __init__(self):
        self.agent = AnswerAgent()

    def execute(self, state: AgentState) -> AgentState:
        return self.agent.generate(state)