#!/usr/bin/python3
""" Delete state objects using sqlalchemy """
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker, Session
from model_state import Base, State

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    s = Session()
    state_result = s.query(State)\
                          .filter(State.name.like('%a%'))\
                          .order_by(State.id.asc())
    for state in state_result:
        s.delete(state)
    s.commit()
