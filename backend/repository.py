from sqlalchemy import create_engine, or_, and_
from sqlalchemy.orm import sessionmaker
from typing import List
from sqlalchemy.exc import IntegrityError

from backend.model import TrainingData, UserDataModel

session = sessionmaker()

class TrainingDataRepository:
    def __init__(self):
        self.session = session

    def insert_user_trainingdata(self, trainingdata: TrainingData):
        try:
            self.session.add(trainingdata)
            self.session.commit()
        except IntegrityError:
            print("Training data already exists.")
            self.session.rollback()

    def retrieve_user_trainingdata(self, uid: int):
        return self.session.query(TrainingData).filter(TrainingData.uid == uid).all()

    def clear_user_trainingdata(self, uid: int):
        self.session.query(TrainingData).filter(TrainingData.uid == uid).delete(synchronize_session='fetch')
        self.session.commit()

class UserDataModelRepository:
    def __init__(self):
        self.session = session

    def insert_user_datamodel(self, datamodel: UserDataModel):
        try:
            self.session.add(datamodel)
            self.session.commit()
        except IntegrityError:
            print("User data model already exists.")
            self.session.rollback()

    def retrieve_user_datamodel(self, uid: int):
        return self.session.query(UserDataModel).filter(UserDataModel.uid == uid).first()

    def update_user_datamodel(self, datamodel: UserDataModel):
        user_datamodel = session.query(UserDataModel).filter(UserDataModel == datamodel).one()
        user_datamodel.datamodel = datamodel.datamodel
        self.session.commit()

    def delete_user_datamodel(self, datamodel: UserDataModel):
        self.session(UserDataModel).filter(UserDataModel == datamodel).delete(synchronize_session='fetch')
        self.session.commit()
