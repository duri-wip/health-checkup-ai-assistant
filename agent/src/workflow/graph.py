from langgraph.graph import StateGraph, END

from src.workflow.state import HealthState
from src.workflow.nodes.classify import classify_question
from src.workflow.nodes.fetch_health import fetch_health_data
from src.workflow.nodes.build_prompt import build_prompt


def build_graph():
    graph = StateGraph(HealthState)

    graph.add_node("classify", classify_question)
    graph.add_node("fetch_health", fetch_health_data)
    graph.add_node("build_prompt", build_prompt)

    graph.set_entry_point("classify")
    graph.add_edge("classify", "fetch_health")
    graph.add_edge("fetch_health", "build_prompt")
    graph.add_edge("build_prompt", END)

    return graph.compile()


graph = build_graph()