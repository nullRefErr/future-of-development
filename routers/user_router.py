from fastapi import APIRouter

from controller.user_controller import create_user_action, login_user_action
from models.user import CreateUserDto, LoginUserDto

router = APIRouter()


@router.post("/user/create", tags=["user"])
async def create_user(data: CreateUserDto):
    return (create_user_action(data))


@router.post("/user/login", tags=["user"])
async def login_user(data: LoginUserDto):
    return (login_user_action(data))
