"""
Tool Executor Node

Executes the tool selected by the router.
"""

from app.graph.state import AgentState
from app.config.logging_config import logger
from app.tools.registry import ToolRegistry

registry = ToolRegistry()


def tool_executor_node(state: AgentState) -> AgentState:
    logger.info("Tool Executor Node Started")

    tool_name = state["selected_tool"]

    logger.info(f"Executing Tool: {tool_name}")

    tool = registry.get_tool(tool_name)

    result = tool.execute(state)

    logger.info("Tool Execution Completed")

    return result