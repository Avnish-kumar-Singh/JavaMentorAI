"""
Answer Node
"""

from app.graph.state import AgentState
from app.services.llm_service import LLMService
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.config.logging_config import logger

llm = LLMService()


def answer_node(state: AgentState) -> AgentState:

    logger.info("Answer Node Started")

    prompt = f"""
{SYSTEM_PROMPT}

User Question:

{state["user_query"]}
"""

    response = llm.invoke(prompt)

    state["response"] = response

    logger.info("Answer Node Completed")

    return state