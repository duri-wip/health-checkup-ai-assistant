from pydantic import BaseModel

class ChatRequest(BaseModel):
    patient_id: str
    question: str
    model: str = "llama3.1:8b"


class ChatResponse(BaseModel):
    answer: str
    question_type: str