from pydantic import BaseModel, ValidationError, field_validator
from fastapi import HTTPException
from crud.user_crud import user_crud

import re


class UserRegister(BaseModel):
    username: str
    email: str
    password: str

    @field_validator('email')
    def email_format_validator(cls, value):
        """
        校验邮箱合法性：
            校验规则：
                @之前1-18长度的字符串，可以是A-Z, a-z, 0-9, _, -字符
                @之后xxx.xxx.xxx.xxx(1-4个xxx.).com/cn
        :param value:
        :return value:
        """
        email_pattern = "[A-Za-z0-9_-]{1,18}.@([A-Za-z0-9-]{1,18}.){1,4}(com|cn)"
        if not re.match(email_pattern, value):
            raise HTTPException(status_code=422, detail='email valid error')
        return value

    @field_validator('email')
    def email_exists_validator(cls, value):
        """
            校验数据库中是否已存在该邮箱
        :param value:
        :return value:
        """
        res = user_crud.get_user_by_email(value)
        if res:
            raise HTTPException(status_code=422, detail='email is already exists')
        return value

