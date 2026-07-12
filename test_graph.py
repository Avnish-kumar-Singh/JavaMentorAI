from app.graph.builder import build_graph

graph = build_graph()

state = {
    "messages": [],
    "user_query": "Explain JVM in simple language.",
    "intent": "",
    "selected_tool": "",
    "context": "",
    "response": "",
    "status": "",
    "error": "",
}

result = graph.invoke(state)

print("\n========== FINAL RESPONSE ==========\n")

print(result["response"])