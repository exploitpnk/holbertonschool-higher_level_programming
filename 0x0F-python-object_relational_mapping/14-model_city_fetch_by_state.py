#!/usr/bin/python3
"""
Write a Python file similar to model_state.py named
model_city.py that contains the class definition of a City.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.name, City.id, City.name).\
        join(City, State.id == City.state_id).\
        order_by(City.id)

    records = query.all()

    for record in records:
        print("{:s}: ({:d}) {:s}".format(*record))

    session.close()
