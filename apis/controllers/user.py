from fastapi import APIRouter
from crud.user_crud import user_crud
from schema.user_schema import UserRegister

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



