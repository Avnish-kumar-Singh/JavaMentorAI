# """
# Planner Agent

# Contains the reasoning logic for deciding the user's intent.
# """

# from app.graph.state import AgentState
# from app.config.logging_config import logger


# class PlannerAgent:

#     def plan(self, state: AgentState) -> AgentState:

#         query = state["user_query"].lower()

#         logger.info("Planner Agent Started")

#         state["intent"] = "general"
#         state["selected_tool"] = "llm"

#         if "spring" in query:
#             state["intent"] = "spring_boot"

#         elif "bug" in query or "error" in query:
#             state["intent"] = "debug"

#         elif "leetcode" in query or "dsa" in query:
#             state["intent"] = "dsa"

#         elif "java 24" in query or "latest java" in query:
#             state["intent"] = "web_search"
#             state["selected_tool"] = "web"

#         elif "pdf" in query or "document" in query:
#             state["intent"] = "rag"
#             state["selected_tool"] = "rag"

#         logger.info(f"Intent: {state['intent']}")
#         logger.info(f"Selected Tool: {state['selected_tool']}")

#         return state




# from app.graph.state import AgentState
# from app.config.logging_config import logger
# from app.core.enums import ToolName, Intent
# 
# 
# class PlannerAgent:
# 
    # def plan(self, state: AgentState) -> AgentState:
# 
        # query = state["user_query"].lower()
# 
        # logger.info("Planner Agent Started")
# 
        # Default route
        # state["intent"] = Intent.GENERAL.value
        # state["selected_tool"] = ToolName.LLM.value
# 
        # Temporary RAG routing for Java-related questions
        # rag_keywords = [
            # "java",
            # "jvm",
            # "spring",
            # "collection",
            # "collections",
            # "hashmap",
            # "arraylist",
            # "linkedlist",
            # "multithreading",
            # "thread",
            # "exception",
            # "jdbc",
            # "hibernate",
            # "rest api",
            # "microservices",
        # ]
# 
        # if any(keyword in query for keyword in rag_keywords):
            # state["intent"] = Intent.RAG.value
            # state["selected_tool"] = ToolName.RAG.value
# 
        # elif "bug" in query or "error" in query:
            # state["intent"] = Intent.DEBUG.value
# 
        # elif "leetcode" in query or "dsa" in query:
            # state["intent"] = Intent.DSA.value
# 
        # elif "java 24" in query or "latest java" in query:
            # state["intent"] = Intent.WEB_SEARCH.value
            # state["selected_tool"] = ToolName.WEB.value
# 
        # elif "pdf" in query or "document" in query:
            # state["intent"] = Intent.RAG.value
            # state["selected_tool"] = ToolName.RAG.value
# 
        # logger.info(f"Intent: {state['intent']}")
        # logger.info(f"Selected Tool: {state['selected_tool']}")
# 
        # return state
        
        
        
"""
Planner Agent

Contains the reasoning logic for deciding the user's intent.
"""

from app.graph.state import AgentState
from app.config.logging_config import logger
from app.core.enums import ToolName, Intent


class PlannerAgent:

    def plan(self, state: AgentState) -> AgentState:

        query = state["user_query"].lower()

        logger.info("Planner Agent Started")

        # ----------------------------
        # Default Route
        # ----------------------------
        state["intent"] = Intent.GENERAL.value
        state["selected_tool"] = ToolName.LLM.value

        # ----------------------------
        # Java Compiler Routing
        # ----------------------------

        # Detect actual Java source code
        if (
            "public class" in query
            or "public static void main" in query
        ):
            state["intent"] = Intent.GENERAL.value
            state["selected_tool"] = ToolName.JAVA_COMPILER.value

        else:

            java_compiler_keywords = [
                "compile",
                "run",
                "execute",
                "java code",
                "compile this",
                "run this",
                "execute this",
            ]

            if any(keyword in query for keyword in java_compiler_keywords):
                state["intent"] = Intent.GENERAL.value
                state["selected_tool"] = ToolName.JAVA_COMPILER.value

            else:

                # ----------------------------
                # RAG Routing
                # ----------------------------
                rag_keywords = [
                    "java",
                    "jvm",
                    "spring",
                    "collection",
                    "collections",
                    "hashmap",
                    "arraylist",
                    "linkedlist",
                    "multithreading",
                    "thread",
                    "exception",
                    "jdbc",
                    "hibernate",
                    "rest api",
                    "microservices",
                ]

                if any(keyword in query for keyword in rag_keywords):
                    state["intent"] = Intent.RAG.value
                    state["selected_tool"] = ToolName.RAG.value

                elif "bug" in query or "error" in query:
                    state["intent"] = Intent.DEBUG.value

                elif "leetcode" in query or "dsa" in query:
                    state["intent"] = Intent.DSA.value

                elif "java 24" in query or "latest java" in query:
                    state["intent"] = Intent.WEB_SEARCH.value
                    state["selected_tool"] = ToolName.WEB.value

                elif "pdf" in query or "document" in query:
                    state["intent"] = Intent.RAG.value
                    state["selected_tool"] = ToolName.RAG.value

        logger.info(f"Intent: {state['intent']}")
        logger.info(f"Selected Tool: {state['selected_tool']}")

        return state