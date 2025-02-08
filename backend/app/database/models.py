from pydantic import BaseModel, EmailStr
from typing import Any, Dict, List, Optional
from bson import ObjectId
from pydantic import BaseModel
from pydantic_core import core_schema
from pydantic.json_schema import JsonSchemaValue
from datetime import datetime

class PyObjectId(str):
    """Custom Pydantic field for MongoDB ObjectId."""

    @classmethod
    def validate(cls, value, info):
        """Ensures the value is a valid MongoDB ObjectId."""
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")
        return str(value)

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler):
        """Ensures compatibility with Pydantic v2 schema."""
        return core_schema.str_schema()

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        """Returns JSON schema format."""
        return JsonSchemaValue(type="string")


# User Model
class User(BaseModel):
    user_id: Optional[int] = None
    username: str
    email: EmailStr
    password: str
    carbon_emissions: List[float] = []  

    class Config:
        orm_mode = True
        json_encoders = {ObjectId: str}

# Carbon footprint log model 
class CarbonFootprint(BaseModel):
    log_id: Optional[int] = None
    user_id: PyObjectId
    date: Optional[str] = str
    
    travel: Optional[Dict[str, Any]] = {
        "start_location": "",
        "end_location": "",
        "mode_of_transport": "",
        "eco_friendly_choice": "",
        "improvement_goal": "",
        "proud_sustainable_action": ""
    }

    car_usage: Optional[Dict[str, Any]] = {
        "used_car": bool,
        "car_type": "",
        "carpool_status": "",
        "route_efficiency_score": 0
    }

    # Public Transport & Shared Rides
    public_transport: Optional[Dict[str, Any]] = {
        "used_public_transport": bool,
        "transport_type": ""
    }

    # Walking/Biking
    active_travel: Optional[Dict[str, Any]] = {
        "walked_or_biked": bool
    }

    # Total Carbon Score Calculation
    total_carbon_score: float = 0.0  # Auto-calculated

    class Config:
        orm_mode = True
        json_encoders = {ObjectId: str}

    
