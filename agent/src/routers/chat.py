import os
import httpx
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from src.schemas.response import ChatRequest
from src.workflow.graph import graph
from src.workflow.call_llm import call_ollama

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")

router = APIRouter(prefix="/chat", tags=["Agent"])


@router.get("/models")
async def get_models():
    try:
        response = httpx.get(f"{OLLAMA_URL}/api/tags", timeout=10)
        response.raise_for_status()
        models = [m["name"] for m in response.json().get("models", [])]
        return {"models": models}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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
            call_ollama(state["prompt"], model=request.model),
            media_type="text/plain",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))