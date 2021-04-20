from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine, or_, and_
from sqlalchemy.orm.exc import NoResultFound

from backend.db import db
from backend.db.model import TrainingData, UserDataModel, UserLogin, PostureData

engine = create_engine('mysql+pymysql://root:123456@localhost/posturechair')
Session = sessionmaker(bind=engine)
session = Session()


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

    def retrieve_all_user_trainingdata(self, uid):
        return self.session.query(TrainingData).filter(TrainingData.uid == uid).all()

    def retrieve_user_classif_trainingdata(self, uid):
        return self.session.query(TrainingData.classification).filter(TrainingData.uid == uid).all()

    def clear_user_trainingdata(self, uid):
        self.session.query(TrainingData).filter(TrainingData.uid == uid).delete(synchronize_session='fetch')
        self.session.commit()


class UserDataModelRepository:
    def __init__(self):
        self.session = session

    def insert_user_datamodel(self, datamodel: UserDataModel):
        try:
            self.session.add(datamodel)
            self.session.commit()
            return 0
        except IntegrityError:
            print("User data model already exists.")
            self.session.rollback()
            return -1

    def retrieve_user_datamodel(self, uid: int):
        return self.session.query(UserDataModel).filter(UserDataModel.uid == uid).first()

    def update_user_datamodel(self, datamodel: UserDataModel):
        try:
            user_datamodel = session.query(UserDataModel).filter(UserDataModel.uid == datamodel.uid).one()
        except NoResultFound:
            try:
                self.session.add(datamodel)
                self.session.commit()
                return 0
            except IntegrityError:
                print("User data model already exists.")
                self.session.rollback()
                return -1
        user_datamodel.datamodel = datamodel.datamodel
        self.session.commit()
        return 0

    def delete_user_datamodel(self, uid: int):
        self.session(UserDataModel).filter(UserDataModel.uid == uid).delete(synchronize_session='fetch')
        self.session.commit()


class PostureDataRepository:
    def __init__(self):
        self.session = session

    def insert_user_posturedata(self, posturedata: PostureData):
        try:
            self.session.add(posturedata)
            self.session.commit()
        except IntegrityError:
            print("Training data already exists.")
            self.session.rollback()

    def retrieve_user_posturedata(self, uid: int):
        return self.session.query(PostureData).filter(PostureData.uid == uid).all()

    def clear_user_posturedata(self, uid: int):
        self.session.query(PostureData).filter(PostureData.uid == uid).delete(synchronize_session='fetch')
        self.session.commit()


class UserLoginRepository:
    def __init__(self):
        self.session = session

    def insert_userlogin(self, userlogin: UserLogin):
        try:
            self.session.add(userlogin)
            self.session.commit()
            return 0
        except IntegrityError:
            print("User data model already exists.")
            self.session.rollback()
            return -1

    def verify_userlogin(self, email, password):
        return self.session.query(UserLogin).filter(UserLogin.email == email, UserLogin.password == password).first()



if __name__ == "__main__":
    repo = UserLoginRepository()
    repo.insert_user_login(UserLogin('test', 'test'))