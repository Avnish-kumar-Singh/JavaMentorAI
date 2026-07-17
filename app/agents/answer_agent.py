# """
# Answer Agent

# Generates the final response using the LLM.
# """

# from app.graph.state import AgentState
# from app.services.llm_service import LLMService
# from app.prompts.system_prompt import SYSTEM_PROMPT
# from app.config.logging_config import logger


# class AnswerAgent:

#     def __init__(self):
#         self.llm = LLMService()

#     def generate(self, state: AgentState) -> AgentState:

#         logger.info("Answer Agent Started")

#         prompt = f"""
# {SYSTEM_PROMPT}

# User Question:

# {state["user_query"]}
# """

#         response = self.llm.invoke(prompt)

#         state["response"] = response

#         logger.info("Answer Agent Finished")

#         return state






# """
# Answer Agent
# """
# 
# from app.graph.state import AgentState
# from app.services.llm_service import LLMService
# from app.prompts.system_prompt import SYSTEM_PROMPT
# from app.config.logging_config import logger
# 
# 
# class AnswerAgent:
# 
    # def __init__(self):
        # self.llm = LLMService()
# 
    # def generate(self, state: AgentState) -> AgentState:
# 
        # logger.info("Answer Agent Started")
# 
        # context = state.get("context", "")
# 
        # prompt = f"""
# {SYSTEM_PROMPT}
# 
# Context:
# {context}
# 
# User Question:
# {state["user_query"]}
# 
# Instructions:
# - Use the context if it is relevant.
# - If the context does not answer the question, answer using your Java knowledge.
# """
# 
        # response = self.llm.invoke(prompt)
# 
        # state["response"] = response
# 
        # logger.info("Answer Agent Finished")
# 
        # return state
        
        
        
"""
Answer Agent
"""

from app.graph.state import AgentState
from app.services.llm_service import LLMService
from app.config.logging_config import logger
from app.synthesis.prompt_builder import PromptBuilder


class AnswerAgent:

    def __init__(self):
        self.llm = LLMService()
        self.prompt_builder = PromptBuilder()

    def generate(self, state: AgentState) -> AgentState:

        logger.info("Answer Agent Started")

        context = state.get("context", "")

        prompt = self.prompt_builder.build(
            question=state["user_query"],
            context=context,
        )

        # response = self.llm.invoke(prompt)
        
        response = self.llm.invoke(
                prompt=prompt,
                question=state["user_query"]
        )

        state["response"] = response

        logger.info("Answer Agent Finished")

        return state