from pydantic import BaseModel

class ChatRequest(BaseModel):
    patient_id: str
    question: str


class ChatResponse(BaseModel):
    answer: str
    question_type: str