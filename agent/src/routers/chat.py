from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from src.schemas.response import ChatRequest
from src.workflow.graph import graph
from src.workflow.call_llm import call_ollama

router = APIRouter(prefix="/chat", tags=["Agent"])

@router.post("/")
async def chat(request: ChatRequest):
    try:
        state = graph.invoke(
            {
                "patient_id": request.patient_id,
                "user_question": request.question,
                "question_type": "",
                "health_data": {},
                "prompt": "",
                "llm_response": "",
            }
        )

        return StreamingResponse(
            call_ollama(state["prompt"]),
            media_type="text/plain",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))