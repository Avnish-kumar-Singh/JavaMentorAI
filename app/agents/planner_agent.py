"""
Planner Agent

Contains the reasoning logic for deciding the user's intent.
"""

from app.graph.state import AgentState
from app.config.logging_config import logger


class PlannerAgent:

    def plan(self, state: AgentState) -> AgentState:

        query = state["user_query"].lower()

        logger.info("Planner Agent Started")

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
        logger.info(f"Selected Tool: {state['selected_tool']}")

        return state