from fastapi import APIRouter, HTTPException
#app.database.database_service import save_carbon_footprint, get_carbon_history
from app.services.openai_services import analyze_carbon_footprint
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

        # ✅ Call OpenAI for carbon analysis
        carbon_score, recommendations = await analyze_carbon_footprint(entry)
        entry["total_carbon_score"] = carbon_score
        entry["recommendations"] = recommendations

        # ✅ Save to database

        return {
            "message": "Carbon footprint submitted successfully",
            "id": 1,
            "carbon_score": carbon_score,
            "recommendations": recommendations
        }

    except Exception as e:
        print("❌ API Error:", str(e))  # ✅ Debugging
        raise HTTPException(status_code=500, detail="Internal Server Error")



