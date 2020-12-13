from backend.Posture import Posture
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, backref, relationship, aliased

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/jokechair')

metadata = MetaData()

conn = engine.connect()

session = sessionmaker(bind=engine)
s = session()


class PostureRepository:

    def __init__(self):
        self.session = s

    @staticmethod
    def create_table():
        posture_table = Table('postures', metadata,
                              Column('user_id', Integer, primary_key=True),
                              Column('datetime', DateTime, primary_key=True),
                              Column('reading_1', Integer),
                              Column('reading_2', Integer),
                              Column('reading_3', Integer),
                              Column('reading_4', Integer),
                              Column('reading_5', Integer),
                              Column('reading_6', Integer),
                              Column('reading_7', Integer),
                              Column('reading_8', Integer),
                              Column('classification', String(20))
                          )
        posture_table.create(engine)


    def insert_posture(self, posture: Posture):
        self.session.add(posture)
        self.session.commit()
        return True

    def get_postures_by_user_id(self, posture: Posture):
        query = self.session.query(Posture).filter(Posture.user_id == posture.user_id)
        return query
