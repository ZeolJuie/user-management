from datetime import timedelta, datetime
from typing import Union

from passlib.context import CryptContext
from jose import JWTError, jwt
from loguru import logger

from crud.user_crud import user_crud


class UserService:

    _pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    _ALGORITHM = "HS256"
    _SECRET_KEY = "c1790b4032161aea9f42f86fee247c198842ea568ee659a34c18222b50810ac8"

    @staticmethod
    def user_login(username, password):
        from datetime import timedelta
        access_token_expires = timedelta(minutes=30)

        hashed_password = user_service.get_user_password(username=username)

        if user_service.verify_password(password, hashed_password):
            access_token = user_service.create_access_token(
                data={"sub": username}, expires_delta=access_token_expires
            )
            return access_token

    def get_password_hash(self, password):
        """
        把密码转为hash密码
        """
        return self._pwd_context.hash(password)

    @staticmethod
    def get_user_password(username):
        return user_crud.get_user_by_username(username)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
            验证输入的密码的hash密码与数据库中记录的hash密码是否是一样的
        :param plain_password: 用户输入的密码
        :param hashed_password: hash密码
        :return:
        """
        return self._pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, data: dict, expires_delta: Union[timedelta, None] = None) -> str:
        """

        :param data:
        :param expires_delta:
        :return:
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, self._SECRET_KEY, algorithm=self._ALGORITHM)
        return encoded_jwt

    def get_current_user(self, token: str):
        """
        解密JWT，即验证JWT字符串的SIGNATURE签名并返回claims(也称PAYLOAD)的信息
        :param token:
        :return:
        """
        try:
            payload = jwt.decode(token, self._SECRET_KEY, algorithms=[self._ALGORITHM])
            # payload = {'sub': 'username', 'exp': 1674033230}
            username: str = payload.get("sub")

            # 在数据库中查询username
            if username is None:
                return None

            user = {
                'username': username,
            }
            return user
        except JWTError as e:
            logger.error(e)


user_service = UserService()
