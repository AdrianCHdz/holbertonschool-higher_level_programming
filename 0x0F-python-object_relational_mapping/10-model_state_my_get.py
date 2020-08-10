#!/usr/bin/python3

from sys import argv
from MySQLdb import connect
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = argv[4]
    query = session.query(State).order_by(State.id).filter(State.name.like(state))
    """
    print("hellow", len(query.all()))
    """
    if query.first():
        for result in query:
            print(f"{result.id}")
    else:
        print("Not found")
    session.close()
