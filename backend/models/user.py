from sqlalchemy import Column, Integer, String, Boolean
from models import BaseModel


class User(BaseModel):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    password = Column(String(160), nullable=False)
    is_active = Column(Boolean(), default=False)
    activation_code = Column(String(160), default=False)
