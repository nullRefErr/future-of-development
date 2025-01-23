from models.user import CreateUserDto, LoginUserDto
from repository.user_collection import get_user_by_email, save_user
from services.helper_service import is_valid_email, is_valid_age, generate_hash


def create_user(data: CreateUserDto):
    is_email_valid = is_valid_email(data.email)
    if is_email_valid not in [True]:
        return {"message": "Invalid email!"}

    is_age_valid = is_valid_age(data.age)
    if is_age_valid not in [True]:
        return {"message": "Invalid age!"}

    check_user = get_user_by_email(data.email)
    if check_user:
        return {"message": "User already exists!"}

    user_data = CreateUserDto(email=data.email, password="", name=data.name, age=data.age)
    user_data.password = generate_hash(data.password)

    save_user(user_data)

    return {"message": "User created successfully!"}


def user_login(data: LoginUserDto):
    is_email_valid = is_valid_email(data.email)
    if is_email_valid not in [True]:
        return {"message": "Invalid email!"}

    check_user = get_user_by_email(data.email)
    if not check_user:
        return {"message": "User does not exist!"}

    hash_password = generate_hash(data.password)

    print(check_user["password"], hash_password)
    if check_user["password"] != hash_password:
        return {"message": "Invalid password!"}

    token = generate_hash("email:" + check_user["email"] + "name:" + check_user["name"])

    return token
