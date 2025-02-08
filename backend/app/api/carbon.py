from fastapi import APIRouter, HTTPException
from app.database.database_service import create_carbon_log, get_carbon_log_by_user
from app.database.models import CarbonFootprint
from typing import Dict, Any

router = APIRouter()

@router.post("/submit")
async def submit_carbon_log(data: CarbonFootprint):
    """
    Stores user's carbon footprint log in the database.
    """
    try:
        print("Received Data:", data.dict())  # ✅ Debugging: Print input data
        log_response = await create_carbon_log(data)
        print("Log Response:", log_response)
        return log_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history")
async def fetch_carbon_logs(user_id: str):
    """
    Fetches all past carbon logs for a user.
    """
    logs = await get_carbon_log_by_user(user_id)
    
    if not logs:
        raise HTTPException(status_code=404, detail="No carbon logs found")
    
    return {"carbon_logs": logs}


