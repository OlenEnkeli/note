from sqlalchemy import *
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class BaseModel(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)

