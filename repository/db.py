from pymongo import MongoClient

from dtos import CreateUserDto

user_collection = None


def startup():
    print('Connecting to database...')
    mongo_client = MongoClient("mongodb://localhost:27002/")
    db = mongo_client["future_agent_db"]
    global user_collection
    user_collection = db["users"]


def get_user_by_email(email: str):
    return user_collection.find_one({"email": email})


def save_user(user: CreateUserDto):
    return user_collection.insert_one({**user.model_dump()})
