from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class ModelBase:
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True, comment='用户ID')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
