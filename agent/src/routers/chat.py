from fastapi import APIRouter, HTTPException

from src.schemas.response import ChatRequest, ChatResponse
from src.workflow.graph import graph
from src.workflow.call_llm import call_ollama

router = APIRouter(prefix="/chat", tags=["Agent"])

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        state = graph.invoke(
            {
                "patient_id": request.patient_id,
                "user_question": request.question,
                "question_type": "",
                "health_data": {},
                "prompt": "",
                "response": "",
            }
        )

        return state 
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))