from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db03_SQLAlchemy_entities import Base, Sensor, Station


def populate(engine):
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    de_bilt = Station(name='De Bilt')
    session.add(de_bilt)
    session.add(Station(name='Utrecht'))
    session.commit()
    print("Station", de_bilt)

    temp_sensor = Sensor(last=20, multiplier=.1, station=de_bilt)
    session.add(temp_sensor)
    session.commit()
    print("Sensor", temp_sensor)


if __name__ == "__main__":
    print("This script is used by code further down in this notebook") 