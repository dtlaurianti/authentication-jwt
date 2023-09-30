from sqlalchemy import Column, String
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class UserLoginInfo(Base):
    __tablename__ = 'user_authentication'
    username = Column(String(20), primary_key=True)
    password = Column(String(20))