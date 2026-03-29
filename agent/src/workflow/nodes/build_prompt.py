from src.workflow.state import HealthState

SYSTEM_PROMPT = """당신은 건강검진 전문 AI 어시스턴트입니다.
항상 답변은 한글로 합니다.
아래 건강검진 데이터와 정상 기준을 바탕으로 사용자의 질문에 친절하고 구체적으로 답변하세요.
- 수치가 정상 범위인지 명확히 언급하세요.
- 이상 소견이 있으면 간단한 생활 습관 개선 조언을 포함하세요.
- 의학적 진단은 내리지 말고, 전문의 상담을 권유하는 방식으로 마무리하세요.
"""


def build_prompt(state: HealthState) -> HealthState:
    data = state["health_data"]
    overview = data["overviewList"][0]
    reference_list = data["referenceList"]
    question_type = state["question_type"]

    FIELD_MAP: dict[str, list[str]] = {
        "cholesterol": ["totalCholesterol", "hdlCholesterol", "ldlCholesterol", "triglyceride"],
        "blood_pressure": ["bloodPressure"],
        "blood_glucose": ["fastingBloodGlucose"],
        "liver": ["ast", "alt", "yGpt"],
        "kidney": ["serumCreatinine", "gfr"],
        "general": list(overview.keys()),
    }

    target_fields = FIELD_MAP.get(question_type, list(overview.keys()))
    filtered_overview = {k: v for k, v in overview.items() if k in target_fields}

    ref_normal = next((r for r in reference_list if r.get("refType") == "정상(A)"), {})
    ref_warning = next((r for r in reference_list if r.get("refType") == "정상(B)"), {})
    ref_danger = next((r for r in reference_list if r.get("refType") == "질환의심"), {})
    filtered_ref = {
        "정상(A)": {k: v for k, v in ref_normal.items() if k in target_fields and v},
        "정상(B)": {k: v for k, v in ref_warning.items() if k in target_fields and v},
        "질환의심": {k: v for k, v in ref_danger.items() if k in target_fields and v},
    }

    state["prompt"] = f"""{SYSTEM_PROMPT}

[정상 기준]
{filtered_ref}

[검진 데이터]
{filtered_overview}

[사용자 질문]
{state['user_question']}
"""
    return state