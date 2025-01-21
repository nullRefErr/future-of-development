from pydantic import BaseModel


class CreateUserDto(BaseModel):
    email: str
    password: str
    name: str
    age: int


class LoginUserDto(BaseModel):
    email: str
    password: str
