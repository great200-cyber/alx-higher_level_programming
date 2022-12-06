#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    s = Session()
    j = 0
    for row in s.query(State).order_by(State.id.asc()):
        if row.name == sys.argv[4]:
            j += 1
            print(row.id)
    if j == 0:
        print("Not found")
    