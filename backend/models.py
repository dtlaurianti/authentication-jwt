from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

with open("config.json", "r") as f:
    config = json.load(f)

connection = (
    f'mysql+mysqlconnector://{config["user"]}:'
    f'{config["password"]}@{config["host"]}:'
    f'{config["port"]}/{config["database"]}'
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