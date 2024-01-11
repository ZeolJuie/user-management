from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import QueuePool
from loguru import logger

import config
from models.user_model import User


class EngineFactory:

    @staticmethod
    def get_engine():
        """获取MySQL的连接"""
        connect_info = {
            "user": config.MYSQL_USER,
            "password": config.MYSQL_PASSWORD,
            "host": config.MYSQL_HOST,
            "db": config.MYSQL_DATABASE
        }
        url = "mysql+pymysql://{user}:{password}@{host}/{db}?charset=utf8".format(**connect_info)
        try:
            _engine = create_engine(url=url,
                                    poolclass=QueuePool,
                                    pool_size=5,
                                    pool_timeout=30,
                                    pool_recycle=3600
                                    )
        except Exception as e:
            logger.error("mysql database connect failed!", e)
        else:
            logger.success("mysql database connect success!")

            return _engine


if __name__ == '__main__':
    engine = EngineFactory.get_engine()
    session = sessionmaker(engine)

    try:
        db_session = session()
        res = db_session.query(User.name).all()
        db_session.commit()
        db_session.close()
    except Exception as e:
        logger.warning(e)
    else:
        for item in res:
            print(item)

