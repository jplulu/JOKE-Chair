from backend.repository.repository import UserDataModelRepository
from backend.db.model import UserDataModel
import joblib

repo = UserDataModelRepository()
pkl = joblib.load("test_clf.pkl")
temp = UserDataModel(2, pkl)
repo.insert_user_datamodel(temp)


