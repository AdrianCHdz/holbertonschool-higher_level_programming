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

    new_data = State(name="Louisiana")
    session.add(new_data)
    session.commit()
    print(new_data.id)
    session.close()
