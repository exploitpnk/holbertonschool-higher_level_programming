#!/usr/bin/python3
"""
Write a script that prints the State object with the
 name passed as argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    state_name = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name == state_name)
    records = query.all()

    if records:
        for record in records:
            print(record.id)
    else:
        print("Not found")
