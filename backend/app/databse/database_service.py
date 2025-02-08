from app.database.db import db
from app.database.models import User
import bcrypt
from db.py import users_collection


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

async def add_carbon_emission(user_id: int, score: float):
    """Append a new carbon footprint score to the user's emissions list."""
    await users_collection.update_one(
        {"user_id": user_id},
        {"$push": {"carbon_emissions": score}}
    )
    return {"message": f"Carbon footprint score {score} added for user {user_id}"}

async def get_user_carbon_emissions(user_id: int):
    """Fetch user's past carbon footprint emissions."""
    user = await users_collection.find_one({"user_id": user_id}, {"carbon_emissions": 1, "_id": 0})
    return user.get("carbon_emissions", []) if user else None