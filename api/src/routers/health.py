from fastapi import APIRouter
from src.schemas.response import ApplicationResponse, ResponseStatus
from src.data.health import get_health_data

router = APIRouter(prefix="/api/health", tags=["health"])


@router.get("/{patient_id}", response_model=ApplicationResponse)
async def get_health(patient_id: str) -> ApplicationResponse:
    data = get_health_data(patient_id)
    return ApplicationResponse(
        status=ResponseStatus.success,
        data=data
    )