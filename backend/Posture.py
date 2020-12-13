from __future__ import annotations
from sqlalchemy import create_engine, Integer, Float, String, Column, DateTime, ForeignKey, PrimaryKeyConstraint, func, text, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from datetime import datetime


Base = declarative_base()


class Posture(Base):
    __tablename__ = 'postures'

    # User ID
    user_id = Column(Integer, primary_key=True)

    # Datetime of the reading
    datetime = Column(DateTime, primary_key=True)

    # Sensor readings
    reading_1 = Column(Integer)
    reading_2 = Column(Integer)
    reading_3 = Column(Integer)
    reading_4 = Column(Integer)
    reading_5 = Column(Integer)
    reading_6 = Column(Integer)
    reading_7 = Column(Integer)
    reading_8 = Column(Integer)

    # Posture classification
    classification = Column(String(20))

    def __init__(self,
                 user_id: int,
                 reading_1: int,
                 reading_2: int,
                 reading_3: int,
                 reading_4: int,
                 reading_5: int,
                 reading_6: int,
                 reading_7: int,
                 reading_8: int,
                 classification: str = None):
        self.user_id = user_id
        self.datetime = datetime.now()
        self.reading_1 = reading_1
        self.reading_2 = reading_2
        self.reading_3 = reading_3
        self.reading_4 = reading_4
        self.reading_5 = reading_5
        self.reading_6 = reading_6
        self.reading_7 = reading_7
        self.reading_8 = reading_8
        self.classification = classification


    def __repr__(self):
        return (
            '''
            <Posture(user_id={}, reading_1={}, reading_2={}, reading_3={}, reading_4={}, reading_5={},
                reading_6={}, reading_7={}, reading_8={}, classification={})>
            '''.format(self.user_id, self.reading_1, self.reading_2, self.reading_3, self.reading_4,
                       self.reading_5, self.reading_6, self.reading_7, self.reading_8, self.classification)
        )