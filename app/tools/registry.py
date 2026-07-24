# """
# Tool Registry
# """

# from app.tools.llm_tool import LLMTool


# class ToolRegistry:

#     def __init__(self):

#         self.tools = {
#             "llm": LLMTool(),
#         }

#     def get_tool(self, tool_name: str):

#         tool = self.tools.get(tool_name)

#         if tool is None:
#             raise ValueError(f"Unknown tool: {tool_name}")

#         return tool




# """
# Tool Registry
# """
# 
# from app.tools.llm_tool import LLMTool
# from app.tools.rag_tool import RAGTool
# 
# from app.core.enums import ToolName
# 
# 
# class ToolRegistry:
# 
    # def __init__(self):
# 
        # self.tools = {
            # ToolName.LLM.value: LLMTool(),
            # ToolName.RAG.value: RAGTool(),
        # }
# 
    # def get_tool(self, tool_name: str):
# 
        # tool = self.tools.get(tool_name)
# 
        # if tool is None:
            # raise ValueError(f"Unknown tool: {tool_name}")
# 
        # return tool
        
        
        
        
        
        
        
"""
Tool Registry
"""

from app.tools.llm_tool import LLMTool
from app.tools.rag_tool import RAGTool
from app.tools.java_compiler_tool import JavaCompilerTool

from app.core.enums import ToolName


class ToolRegistry:

    def __init__(self):

        self.tools = {
            ToolName.LLM.value: LLMTool(),
            ToolName.RAG.value: RAGTool(),
            ToolName.JAVA_COMPILER.value: JavaCompilerTool(),
        }

    def get_tool(self, tool_name: str):

        tool = self.tools.get(tool_name)

        if tool is None:
            raise ValueError(f"Unknown tool: {tool_name}")

        return tool