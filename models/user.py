from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class CreateUserDto(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    name: str = Field(min_length=1)
    age: int = Field(ge=0)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "user@example.com",
                    "password": "strongpassword123",
                    "name": "John Doe",
                    "age": 25
                }
            ]
        }
    }


class LoginUserDto(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "user@example.com",
                    "password": "strongpassword123"
                }
            ]
        }
    } 