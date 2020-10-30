#!/usr/bin/python3
"""
Changes the name of a State 
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

    up_id = 2
    name_new = "New Mexico"

    records = session.query(State).filter(State.id == up_id)
    for record in records:
        record.name = name_new

    session.commit()

    session.close()
