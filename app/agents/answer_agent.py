# """
# Answer Agent
# """


# from app.services.response_planner import ResponsePlanner
# from app.graph.state import AgentState
# from app.services.llm_service import LLMService
# from app.config.logging_config import logger
# from app.synthesis.prompt_builder import PromptBuilder


# class AnswerAgent:


#     def __init__(self):
#         self.llm = LLMService()
#         self.prompt_builder = PromptBuilder()
#         self.response_planner = ResponsePlanner()


#     def generate(self, state: AgentState) -> AgentState:


#         logger.info("Answer Agent Started")


#         question = state["user_query"]
#         context = state.get("context", "")
#         history = state.get("messages", [])


#         # Generate response plan
#         response_plan = self.response_planner.plan(question)


#         # Build prompt (now includes prior conversation turns)
#         prompt = self.prompt_builder.build(
#             question=question,
#             context=context,
#             response_plan=response_plan,
#             history=history,
#         )


#         # Generate response
#         response = self.llm.invoke(
#             prompt=prompt,
#             question=question,
#             max_tokens=response_plan["max_tokens"],
#         )


#         state["response"] = response


#         logger.info("Answer Agent Finished")


#         return state



"""
Answer Agent
"""


from app.services.response_planner import ResponsePlanner
from app.graph.state import AgentState
from app.services.llm_service import LLMService
from app.config.logging_config import logger
from app.synthesis.prompt_builder import PromptBuilder


class AnswerAgent:


    def __init__(self):
        self.llm = LLMService()
        self.prompt_builder = PromptBuilder()
        self.response_planner = ResponsePlanner()


    def generate(self, state: AgentState) -> AgentState:


        logger.info("Answer Agent Started")


        question = state["user_query"]
        context = state.get("context", "")
        history = state.get("messages", [])


        # Generate response plan
        response_plan = self.response_planner.plan(question)


        # Build prompt (history always included; PromptBuilder's
        # strict rules prevent unrelated topics from bleeding in,
        # while still allowing follow-ups like "give the corrected
        # code" to correctly resolve to the last turn's content)
        prompt = self.prompt_builder.build(
            question=question,
            context=context,
            response_plan=response_plan,
            history=history,
        )


        # Generate response
        response = self.llm.invoke(
            prompt=prompt,
            question=question,
            max_tokens=response_plan["max_tokens"],
        )


        state["response"] = response


        logger.info("Answer Agent Finished")


        return state