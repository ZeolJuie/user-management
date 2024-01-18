from fastapi import APIRouter, Depends, Header, HTTPException
from fastapi.security import OAuth2PasswordBearer

from crud.user_crud import user_crud
from schema.user_schema import UserRegister, UserLogin
from service.user_service import user_service

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


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
    password = login_info.password
    username = login_info.username

    accesstoken = user_service.user_login(username, password)
    if not accesstoken:
        return HTTPException(status_code=401, detail="Login failed")
    return accesstoken


@router.post('/token', tags=['用户管理'])
def test_jwt_token(token: str = Depends(oauth2_scheme)):
    print(token)
    user = user_service.get_current_user(token=token)
    if not user:
        return HTTPException(status_code=401, detail="Authoritarian failed")
    return user



