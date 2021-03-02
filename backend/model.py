from datetime import datetime

from sqlalchemy.dialects.mysql import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, ForeignKey, create_engine, BLOB, MetaData
from sqlalchemy.types import Text, JSON, LargeBinary, String, PickleType
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import OperationalError

Base = declarative_base()

class TrainingData(Base):
    __tablename__ = "trainingdata"

    uid = Column(Integer, primary_key=True)
    timestamp = Column(TIMESTAMP, primary_key=True)
    sensor1 = Column(Integer)
    sensor2 = Column(Integer)
    sensor3 = Column(Integer)
    sensor4 = Column(Integer)
    sensor5 = Column(Integer)
    sensor6 = Column(Integer)
    sensor7 = Column(Integer)
    sensor8 = Column(Integer)
    classification = Column(String)

    def __init__(self, uid, timestamp, sensor1, sensor2, sensor3,
                 sensor4, sensor5, sensor6, sensor7, sensor8, classification):
        self.uid = uid
        self.timestamp = timestamp
        self.sensor1 = sensor1
        self.sensor2 = sensor2
        self.sensor3 = sensor3
        self.sensor4 = sensor4
        self.sensor5 = sensor5
        self.sensor6 = sensor6
        self.sensor7 = sensor7
        self.sensor8 = sensor8
        self.classification = classification

    def __repr__(self):
        return "<TrainingData(uid=%s, timestamp=%s, sensor1=%s, sensor2=%s, sensor3=%s, sensor4=%s" \
               ", sensor5=%s, sensor6=%s, sensor7=%s, sensor8=%s, classification=%s)>" % (self.uid, self.timestamp,
        self.sensor1, self.sensor2, self.sensor3, self.sensor4, self.sensor5, self.sensor6, self.sensor7, self.sensor8,
                                                                                          self.classification)


class UserDataModel(Base):
    __tablename__ = "userdatamodel"

    uid = Column(Integer, primary_key=True)
    datamodel = Column(PickleType)

    def __init__(self, uid, datamodel):
        self.uid = uid
        self.datamodel = datamodel

    def __repr__(self):
        return "<UserDataModel(uid=%s, datamodel=%s)>" % (self.uid, self.datamodel)




