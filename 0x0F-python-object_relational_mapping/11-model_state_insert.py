#!/usr/bin/python3
"""
Adds the State object “Louisiana”
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    name_new = "Louisiana"
    newState = State(name=name_new)
    session.add(newState)
    session.commit()

    print(newState.id)

    session.close()
