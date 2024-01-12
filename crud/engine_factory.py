from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import QueuePool
from loguru import logger

import config
from models.user_model import User


class SessionFactory:

    _engine = None
    _session = None

    def __init__(self):
        """获取MySQL的连接"""
        connect_info = {
            "user": config.MYSQL_USER,
            "password": config.MYSQL_PASSWORD,
            "host": config.MYSQL_HOST,
            "db": config.MYSQL_DATABASE
        }
        url = "mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8".format(**connect_info)
        try:
            self._engine = create_engine(url=url,
                                         poolclass=QueuePool,
                                         pool_size=5,
                                         pool_timeout=30,
                                         pool_recycle=3600
                                         )
        except Exception as e:
            logger.error("mysql database connect failed!", e)
        else:
            logger.success("mysql database connect success!")
            self._session = sessionmaker(self._engine)

    def get_session(self):
        """获取一个会话实例"""
        try:
            db_session = self._session()
        except Exception as e:
            logger.warning(e)
        else:
            logger.success('get session success!')
            return db_session


session_factory = SessionFactory()




