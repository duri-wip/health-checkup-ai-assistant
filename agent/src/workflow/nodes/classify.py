from src.workflow.state import HealthState

def classify_question(state: HealthState) -> HealthState:
    question = state["user_question"]

    if "콜레스테롤" in question or "HDL" in question or "LDL" in question or "중성지방" in question:
        state["question_type"] = "cholesterol"
    elif "혈압" in question or "수축기" in question or "이완기" in question:
        state["question_type"] = "blood_pressure"
    else:
        state["question_type"] = "general"

    return state

