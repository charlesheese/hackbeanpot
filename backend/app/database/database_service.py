from app.database.connections import db
from app.database.models import PyObjectId, User
import bcrypt
from app.database.connections import users_collection
from app.database.connections import carbon_collection
from app.database.models import CarbonFootprint

async def get_next_user_id():
    """Get the next user ID"""
    last_user = await db.users.find_one({}, sort=[("user_id", -1)])
    return last_user["user_id"] + 1 if last_user else 1

from app.database.connections import users_collection
from app.database.models import User
import bcrypt


async def create_user(user: User):
    """Create a new user"""
    user_id = await get_next_user_id()  
    
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    user_data = user.dict()
    user_data["hashed_password"] = hashed_password
    user_data["user_id"] = user_id  
    del user_data["password"]  # ✅ Ensure raw password is not stored

    result = await users_collection.insert_one(user_data)  # ✅ Use users_collection
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

async def get_next_log_id():
    """Get the next log ID by finding the highest current ID and incrementing."""
    last_log = await carbon_collection.find_one({}, sort=[("log_id", -1)])
    return last_log["log_id"] + 1 if last_log else 1

from bson import ObjectId
from datetime import datetime

async def create_carbon_log(carbon_log: CarbonFootprint):
    """Create a new carbon footprint log entry in MongoDB."""
    log_id = await get_next_log_id()
    
    log_data = carbon_log.dict()
    log_data["log_id"] = log_id  # Assign auto-incremented log ID

    print("🟢 Preparing to insert into MongoDB:", log_data)  # Debugging

    try:
        result = await carbon_collection.insert_one(log_data)
        print("✅ MongoDB Inserted:", result.inserted_id)  # Debugging Success
        return {"message": "Carbon log created", "log_id": str(result.inserted_id)}
    except Exception as e:
        print("❌ MongoDB Insert Error:", e)  # Debugging Error
        raise HTTPException(status_code=500, detail=f"MongoDB Insert Error: {str(e)}")



async def get_carbon_log_by_user(user_id: str):
    """Retrieve all carbon footprint logs for a user."""
    logs = await carbon_collection.find({"user_id": PyObjectId(user_id)}).to_list(100)
    return logs