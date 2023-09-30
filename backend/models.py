from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import json
from database.orm_models import Base, UserLoginInfo

with open("config.json", "r") as f:
    config = json.load(f)["database"]

print(config)

connection = (
    f'mysql+mysqlconnector://{config["user"]}:'
    f'{config["password"]}@{config["host"]}:'
    f'{config["port"]}/{config["database_name"]}'
)

engine = create_engine(connection)
session_maker = sessionmaker(bind=engine)

# any function that uses the database should be decorated with this to manage session
def session_decorator(func):
    def wrapper(*args, **kwargs):
        session = session_maker()
        res = func(session, *args, **kwargs)
        session.close()
        return res
    return wrapper

@session_decorator
def verify_login(session: Session, username: str, password: str):
    user = session.query(UserLoginInfo).filter_by(username=username).first()
    if user is None:
        return False
    return user.password == password
    
@session_decorator
def register_user(session: Session, username: str, password: str):
    user = session.query(UserLoginInfo).filter_by(username=username).first()
    if user is not None:
        return False
    session.add(UserLoginInfo(username=username, password=password))
    session.commit()
    return True