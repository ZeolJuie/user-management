from fastapi import APIRouter, Depends
from crud.user_crud import user_crud
from schema.user_schema import UserRegister, UserLogin
from service.user_service import user_service

router = APIRouter()


@router.get('/', tags=['用户管理'])
def get_all_users():
    print('request')
    res = user_crud.get_all_users()
    return {item[0]: item[1] for item in res}


@router.post('/register', tags=['用户管理'])
def register(register_info: UserRegister):
    """
    注册用户
    :param register_info: 用户注册信息
    :return:
    """
    email = register_info.email

    return


@router.post('/login', tags=['用户管理'])
def login(login_info: UserLogin):
    """
        用户登录
    :param login_info:
    :return:
    """
    from datetime import timedelta
    access_token_expires = timedelta(minutes=30)

    password = login_info.password
    hashed_password = user_service.get_password_hash(password)

    if user_service.verify_password(password, hashed_password):
        access_token = user_service.create_access_token(
            data={"sub": login_info.username}, expires_delta=access_token_expires
        )
        return access_token


@router.post('/me/{token}', tags=['用户管理'])
def test_jwt_token(token: str):
    return user_service.get_current_user(token)


