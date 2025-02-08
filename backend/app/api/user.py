from fastapi import APIRouter, HTTPException
from app.database.database_service import create_user, get_user_by_email
from app.database.models import User

router = APIRouter()

@router.post("/signup")
async def signup(user: User):
    """Registers a new user and stores them in MongoDB."""
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_response = await create_user(user)
    return user_response