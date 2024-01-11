from sqlalchemy import String
from sqlalchemy import Column
from models.base_model import ModelBase


class User(ModelBase):

    __tablename__ = 'user'

    name = Column(String(length=128), comment='用户名')
    email = Column(String(length=128), comment='用户邮箱')
    # password = Column(String(length=128), comment='用户密码')

