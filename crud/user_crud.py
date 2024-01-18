import time

from loguru import logger

from crud.engine_factory import session_factory
from models.user_model import User


class UserCrud:

    def __init__(self):
        self._session = session_factory.get_session()

    def get_all_users(self):
        try:
            result = self._session.query(User.name, User.email).all()
            self._session.commit()
            self._session.close()
        except Exception as e:
            logger.warning(e)
        else:
            return result

    def get_user_by_email(self, email):
        try:
            result = self._session.query(User.email).filter_by(email=email).all()
            self._session.commit()
            self._session.close()
        except Exception as e:
            logger.warning(e)
        else:
            return result

    # TODO 将几个接口合并成get_user_by_condition
    def get_user_by_username(self, username):
        try:
            result = self._session.query(User.password).filter_by(name=username).all()
            self._session.commit()
            self._session.close()
        except Exception as e:
            logger.warning(e)
        else:
            return result[0][0]


user_crud = UserCrud()


if __name__ == '__main__':
    print(user_crud.get_all_users())
