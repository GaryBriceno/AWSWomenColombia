# SQLAlchemy is a object-relational mapping
# Realiza el mapping entre una base de datos relacional y los objetos
# Se agrega una capa adicional de abstraccion
# Utilizamos SQLAlchemy en lugar de utilizar comandos SQL

from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import UniqueConstraint

Base = declarative_base()


class Station(Base):
    __tablename__ = 'station'
    id = Column(Integer, primary_key=True)
    name = Column(String(14), nullable=False, unique=True)

    def __repr__(self):
        return "Id=%d name=%s" % (self.id, self.name)


class Sensor(Base):
    __tablename__ = 'sensor'
    id = Column(Integer, primary_key=True)
    last = Column(Integer)
    multiplier = Column(Float)
    station_id = Column(Integer, ForeignKey('station.id'))
    station = relationship(Station)

    def __repr__(self):
        return f"Id={self.id} last=se{self.last} " \
               f"multiplier={self.multiplier} " \
               f"station_id={self.station_id}"


if __name__ == "__main__":
    print("This script is used by code further down in this notebook.")