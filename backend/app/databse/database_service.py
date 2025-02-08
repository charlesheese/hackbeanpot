from app.database.db import db
from app.database.models import User
import bcrypt

async def get_next_user_id():
    """Get the next user ID"""
    last_user = await db.users.find_one({}, sort=[("user_id", -1)])
    return last_user["user_id"] + 1 if last_user else 1

async def create_user(user: User):
    """Create a new user"""
    user_id = await get_next_user_id()  
    
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    user_data = user.dict()
    user_data["hashed_password"] = hashed_password
    user_data["user_id"] = user_id  
    del user_data["password"]  

    result = await db.users.insert_one(user_data)
    return {"message": "User created", "id": str(result.inserted_id), "user_id": user_id}

async def get_user_by_email(email: str):
    """Fetch user details by email."""
    return await db.users.find_one({"email": email}, {"_id": 0, "username": 1, "email": 1, "user_id": 1})
