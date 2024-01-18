from fastapi import APIRouter
from crud.user_crud import user_crud
from models.user_model import User
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
    # TODO 在service层完整user实例的构造
    user = User()
    user.name = register_info.username
    user.email = register_info.email

    # TODO 返回http状态
    return user_crud.add_user(user)



