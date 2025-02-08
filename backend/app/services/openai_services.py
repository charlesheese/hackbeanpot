from fastapi import APIRouter, HTTPException
from database.carbon_crud import save_carbon_footprint, get_carbon_history
from app.services.openai_service import analyze_carbon_footprint
from pydantic import BaseModel
from typing import Dict, Any

router = APIRouter()

class CarbonSubmission(BaseModel):
    user_id: str
    travel: Dict[str, Any]
    car_usage: Dict[str, Any]
    public_transport: Dict[str, Any]
    active_travel: Dict[str, Any]

@router.post("/submit")
async def submit_carbon_footprint(data: CarbonSubmission):
    """
    Processes user's carbon footprint and returns OpenAI insights.
    """
    try:
        entry = data.dict()
        
        # Call OpenAI to analyze data
        entry["total_carbon_score"], entry["recommendations"] = await analyze_carbon_footprint(entry)

        # Save to database
        doc_id = await save_carbon_footprint(entry)

        return {
            "message": "Carbon footprint submitted successfully",
            "id": doc_id,
            "carbon_score": entry["total_carbon_score"],
            "recommendations": entry["recommendations"]
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history")
async def fetch_carbon_history(user_id: str):
    """
    Fetches past carbon footprint submissions for a user.
    """
    records = await get_carbon_history(user_id)
    
    if not records:
        raise HTTPException(status_code=404, detail="No history found")
    
    return {"history": records}
