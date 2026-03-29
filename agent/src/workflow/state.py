from typing import Any
from typing_extensions import TypedDict


class HealthState(TypedDict):
    patient_id: str
    user_question: str
    question_type: str        
    health_data: dict[str, Any]
    prompt: str
    llm_response: str