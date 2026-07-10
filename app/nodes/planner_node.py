"""
Planner Node

Responsible for understanding the user's intent.
"""

from app.graph.state import AgentState
from app.config.logging_config import logger


def planner_node(state: AgentState) -> AgentState:
    """
    Analyze the user query and determine the intent.
    """

    query = state["user_query"].lower()

    logger.info("Planner Node Started")

    # Default values
    state["intent"] = "general"
    state["selected_tool"] = "llm"

    if "spring" in query:
        state["intent"] = "spring_boot"

    elif "bug" in query or "error" in query:
        state["intent"] = "debug"

    elif "leetcode" in query or "dsa" in query:
        state["intent"] = "dsa"

    elif "java 24" in query or "latest java" in query:
        state["intent"] = "web_search"
        state["selected_tool"] = "web"

    elif "pdf" in query or "document" in query:
        state["intent"] = "rag"
        state["selected_tool"] = "rag"

    logger.info(f"Intent: {state['intent']}")
    logger.info(f"Tool: {state['selected_tool']}")

    return state