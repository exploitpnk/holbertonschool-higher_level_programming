#!/usr/bin/python3
"""
lists all City objects
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City).order_by(City.id)

    cities = query.all()

    for city in cities:
        print("{:d}: {:s} -> {:s}".
              format(city.id, city.name, city.state.name))

    session.close()
