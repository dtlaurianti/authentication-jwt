#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm_models import Base, UserLoginInfo
import json
import os

script_working_directory = os.path.dirname(os.path.realpath(__file__))
path_to_config = os.path.join(script_working_directory, "../config.json")

# import the database configuration from config.json
with open(path_to_config, "r") as f:
    config = json.load(f)["database"]

# interpolate the connection URL
connection = (
    f'mysql+mysqlconnector://{config["user"]}:'
    f'{config["password"]}@{config["host"]}:'
    f'{config["port"]}/{config["database_name"]}'
)

# generate the database schema and enter a few example users
engine = create_engine(connection)

Base.metadata.create_all(engine)

setup_session_maker = sessionmaker(bind=engine)
setup_session = setup_session_maker()

setup_session.add_all([
    UserLoginInfo(username="user1", password="123456"),
    UserLoginInfo(username="user2", password="234567"),
    UserLoginInfo(username="user3", password="345678"),
    UserLoginInfo(username="user4", password="456789"),
    UserLoginInfo(username="user5", password="567890")
])

setup_session.commit()
setup_session.close()
