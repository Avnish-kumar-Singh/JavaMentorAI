"""
Tool Registry
"""

from app.tools.llm_tool import LLMTool


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "llm": LLMTool(),
        }

    def get_tool(self, tool_name: str):

        tool = self.tools.get(tool_name)

        if tool is None:
            raise ValueError(f"Unknown tool: {tool_name}")

        return tool