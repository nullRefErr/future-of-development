from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from dotenv import load_dotenv

from dtos import CreateUserDto

load_dotenv()

user_collection = None


def startup():
    try:
        print('Connecting to database...')
        mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27002/")
        db_name = os.getenv("DB_NAME", "future_agent_db")
        
        mongo_client = MongoClient(mongo_url)
        # Test the connection
        mongo_client.admin.command('ping')
        
        db = mongo_client[db_name]
        global user_collection
        user_collection = db["users"]
        
        print(f"Successfully connected to MongoDB at {mongo_url}")
    except ConnectionFailure as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise e
    except Exception as e:
        print(f"An error occurred while connecting to MongoDB: {e}")
        raise e
