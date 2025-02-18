import os
import random
import uuid
from datetime import datetime, timedelta

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

load_dotenv()

global user_collection
global livestream_collection
global message_collection
global spam_collection

try:
    print('Connecting to database...')
    mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27002/")
    db_name = os.getenv("DB_NAME", "future_agent_db")

    mongo_client = MongoClient(mongo_url)
    # Test the connection
    mongo_client.admin.command('ping')

    db = mongo_client[db_name]

    user_collection = db["users"]
    livestream_collection = db["livestreams"]
    message_collection = db["messages"]
    spam_collection = db["spams"]

    # generate_fake_user_data()
    # generate_fake_livestream_data()
    # generate_fake_message_data()

    print(f"Successfully connected to MongoDB at {mongo_url}")
except ConnectionFailure as e:
    print(f"Failed to connect to MongoDB: {e}")
    raise e
except Exception as e:
    print(f"An error occurred while connecting to MongoDB: {e}")
    raise e


def generate_fake_user_data():
    count = user_collection.count_documents({})
    if count > 0:
        print("User data already exists in the database.")
        return
    # Sample data generation
    names = ["John", "Jane", "Michael", "Sarah", "David", "Emily", "James", "Alice", "Robert", "Olivia"]
    surnames = ["Doe", "Smith", "Johnson", "Brown", "Wilson", "Taylor", "Anderson", "Lee", "Clark", "Lewis"]
    premium_status = ["PREMIUM", "IDLE", "NONE"]

    # Create 1000 records
    user_data = []
    for _ in range(1000):
        user = {
            "_id": str(uuid.uuid4()),  # Random UUID for MongoDB _id
            "name": random.choice(names),
            "surname": random.choice(surnames),
            "email": f"{random.choice(names).lower()}{random.choice(surnames).lower()}@example.com",
            "phone": f"+{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
            "trust_score": random.randint(0, 100),
            "blocked_numbers": [],
            "premium_status": random.choice(premium_status)
        }
        user_data.append(user)
    # Insert data into MongoDB
    user_collection.insert_many(user_data)
    print(f"Successfully populated users")


def generate_fake_livestream_data():
    count = livestream_collection.count_documents({})
    if count > 0:
        print("livestream data already exists in the database.")
        return

    users = user_collection.find({}).limit(10)
    owner_ids = [user["_id"] for user in users]
    now = datetime.now()
    livestream_data = []
    for _ in range(1000):
        owner = random.choice(owner_ids)
        created_at = now - timedelta(days=random.randint(0, 30))  # Random timestamp within the last 30 days
        ended_at = created_at + timedelta(
            minutes=random.randint(10, 120))  # Random stream duration between 10-120 minutes
        duration = (ended_at - created_at).seconds // 60  # Duration in minutes

        livestream = {
            "owner_id": owner,
            "created_at": created_at,
            "ended_at": ended_at,
            "duration": duration
        }
        livestream_data.append(livestream)

    # Insert data into MongoDB
    livestream_collection.insert_many(livestream_data)
    print(f"Successfully populated livestreams")


def generate_fake_message_data():
    count = message_collection.count_documents({})
    if count > 0:
        print("Message data already exists in the database.")
        return

    users = user_collection.find({})
    owner_ids = [user["_id"] for user in users]

    # Sample messages
    sample_messages = [
        "Hey, how are you?",
        "Did you get the document?",
        "Let's meet tomorrow at 6!",
        "Can you send me the report?",
        "Happy Birthday!",
        "Don't forget the meeting at 3 PM.",
        "Can you call me when you're free?",
        "Here's the link I promised.",
        "I'll be there in 10 minutes.",
        "What time does the event start?"
    ]

    # Create 1000 message records
    message_data = []
    now = datetime.now()

    for _ in range(10000):
        from_id = random.choice(owner_ids)
        to_id = random.choice(owner_ids)
        message = random.choice(sample_messages)  # Random message
        created_at = now - timedelta(days=random.randint(0, 30))  # Random timestamp within the last 30 days

        message_record = {
            "_id": str(uuid.uuid4()),
            "from_id": from_id,
            "to_id": to_id,
            "message": message,
            "created_at": created_at
        }
        message_data.append(message_record)

    # Insert data into MongoDB
    message_collection.insert_many(message_data)
    print(f"Successfully populated messages")


def get_messages(from_id, to_id):
    return message_collection.find({"from_id": from_id, "to_id": to_id})


def save_message(from_id: str, to_id: str, message: str):
    return message_collection.insert_one(
        {"from_id": from_id, "to_id": to_id, "message": message, "created_at": datetime.now()})


def add_spam(userId, phone):
    spam_collection.insert_one({"userId": userId, "phone": phone})


def check_for_spam(phone):
    return spam_collection.count_documents({"phone": phone})


def get_user_by_phone(phone):
    return user_collection.find_one({"phone": phone})


def get_user_by_id(id):
    return user_collection.find_one({"_id": id})


def block_number(_id: str, phone_number: str):
    user_collection.update_one({"_id": _id}, {"$addToSet": {"blocked_numbers": phone_number}})


def get_trust_score(_id: str):
    user = user_collection.find_one({"_id": _id})
    return user["trust_score"]


def get_status(_id: str):
    user = user_collection.find_one({"_id": _id})
    return user["premium_status"]
