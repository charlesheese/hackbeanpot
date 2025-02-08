from motor import motor_asyncio 
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["carbon_footprint"]

users_collection = db["users"]
carbon_collection = db["carbon_footprints"]