from dtos import CreateUserDto, LoginUserDto
from services.user_service import create_user, user_login


def create_user_action(data: CreateUserDto):
    return create_user(data)


def login_user_action(data: LoginUserDto):
    return user_login(data)
