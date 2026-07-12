"""
LangGraph Builder
"""

from langgraph.graph import StateGraph, START, END

from app.graph.state import AgentState
from app.nodes.planner_node import planner_node
from app.nodes.answer_node import answer_node


def build_graph():

    builder = StateGraph(AgentState)

    builder.add_node("planner", planner_node)
    builder.add_node("answer", answer_node)

    builder.add_edge(START, "planner")
    builder.add_edge("planner", "answer")
    builder.add_edge("answer", END)

    return builder.compile()