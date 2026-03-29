from src.workflow.state import HealthState

def classify_question(state: HealthState) -> HealthState:
    question = state["user_question"]

    if any(k in question for k in ["콜레스테롤", "HDL", "LDL", "중성지방", "triglyceride"]):
        state["question_type"] = "cholesterol"
    elif any(k in question for k in ["혈압", "수축기", "이완기"]):
        state["question_type"] = "blood_pressure"
    elif any(k in question for k in ["혈당", "공복혈당", "혈당수치", "당뇨"]):
        state["question_type"] = "blood_glucose"
    elif any(k in question for k in ["간", "AST", "ALT", "GPT", "간수치"]):
        state["question_type"] = "liver"
    elif any(k in question for k in ["신장", "크레아티닌", "GFR", "신기능", "콩팥"]):
        state["question_type"] = "kidney"
    else:
        state["question_type"] = "general"

    return state

