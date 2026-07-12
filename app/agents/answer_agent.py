"""
Answer Agent

Generates the final response using the LLM.
"""

from app.graph.state import AgentState
from app.services.llm_service import LLMService
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.config.logging_config import logger


class AnswerAgent:

    def __init__(self):
        self.llm = LLMService()

    def generate(self, state: AgentState) -> AgentState:

        logger.info("Answer Agent Started")

        prompt = f"""
{SYSTEM_PROMPT}

User Question:

{state["user_query"]}
"""

        response = self.llm.invoke(prompt)

        state["response"] = response

        logger.info("Answer Agent Finished")

        return state