# """
# LangGraph Builder
# """

# from langgraph.graph import StateGraph, START, END

# from app.graph.state import AgentState
# from app.nodes.planner_node import planner_node
# from app.nodes.answer_node import answer_node


# def build_graph():

#     builder = StateGraph(AgentState)

#     builder.add_node("planner", planner_node)
#     builder.add_node("answer", answer_node)

#     builder.add_edge(START, "planner")
#     builder.add_edge("planner", "answer")
#     builder.add_edge("answer", END)

#     return builder.compile()





# from langgraph.graph import StateGraph, START, END
# 
# from app.graph.state import AgentState
# 
# from app.nodes.planner_node import planner_node
# from app.nodes.router_node import router_node
# from app.nodes.answer_node import answer_node
# 
# from app.graph.router import route
# 
# 
# def build_graph():
# 
    # builder = StateGraph(AgentState)
# 
    # builder.add_node("planner", planner_node)
    # builder.add_node("router", router_node)
    # builder.add_node("answer", answer_node)
# 
    # builder.add_edge(START, "planner")
    # builder.add_edge("planner", "router")
# 
    # builder.add_conditional_edges(
        # "router",
        # route,
        # {
            # "answer": "answer"
        # }
    # )
# 
    # builder.add_edge("answer", END)
# 
    # return builder.compile()
    
    
    
    
    
# from langgraph.graph import StateGraph, START, END
# 
# from app.graph.state import AgentState
# from app.nodes.planner_node import planner_node
# from app.nodes.router_node import router_node
# 
# 
# def build_graph():
# 
    # builder = StateGraph(AgentState)
# 
    # builder.add_node("planner", planner_node)
    # builder.add_node("router", router_node)
# 
    # builder.add_edge(START, "planner")
    # builder.add_edge("planner", "router")
    # builder.add_edge("router", END)
# 
    # return builder.compile()
    
    
    
    
    
from langgraph.graph import StateGraph, START, END

from app.graph.state import AgentState

from app.nodes.planner_node import planner_node
from app.nodes.router_node import router_node
from app.nodes.tool_executor_node import tool_executor_node


def build_graph():

    builder = StateGraph(AgentState)

    builder.add_node("planner", planner_node)
    builder.add_node("router", router_node)
    builder.add_node("tool_executor", tool_executor_node)

    builder.add_edge(START, "planner")
    builder.add_edge("planner", "router")
    builder.add_edge("router", "tool_executor")
    builder.add_edge("tool_executor", END)

    return builder.compile()