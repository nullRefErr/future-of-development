from dtos import CreateUserDto
from repository.db import user_collection


def get_user_by_email(email: str):
    if not user_collection:
        raise RuntimeError("Database not initialized. Call startup() first.")
    return user_collection.find_one({"email": email})


def save_user(user: CreateUserDto):
    if not user_collection:
        raise RuntimeError("Database not initialized. Call startup() first.")
    return user_collection.insert_one({**user.model_dump()})
