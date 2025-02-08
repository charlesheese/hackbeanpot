from fastapi import APIRouter, HTTPException
from database.carbon_crud import save_carbon_footprint, get_carbon_history
from app.services.openai_service import analyze_carbon_footprint
from pydantic import BaseModel

router = APIRouter()

class CarbonSubmission(BaseModel):
    user_id: str
    transportation: dict
    diet: str
    electricity_usage: str
    other_factors: str

@router.post("/submit")
async def submit_carbon_footprint(data: CarbonSubmission):
    """
    Processes user's carbon footprint and returns OpenAI insights.
    """
    try:
        entry = data.dict()
        
        # Call OpenAI to analyze data
        entry["carbon_score"], entry["recommendations"] = await analyze_carbon_footprint(entry)

        # Save to database (MongoDB integration can be added later)
        doc_id = await save_carbon_footprint(entry)

        return {
            "message": "Carbon footprint submitted successfully",
            "id": doc_id,
            "carbon_score": entry["carbon_score"],
            "recommendations": entry["recommendations"]
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
