import os
import httpx
from src.workflow.state import HealthState

MOCK_API_URL = os.getenv("MOCK_API_URL")

def fetch_health_data(state: HealthState) -> HealthState:
    patient_id = state["patient_id"]
    response = httpx.get(f"{MOCK_API_URL}/api/health/{patient_id}")
    response.raise_for_status()
    state["health_data"] = response.json()["data"]
    return state