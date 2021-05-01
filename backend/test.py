from backend.repository.repository import UserDataModelRepository
from backend.db.model import UserDataModel
import joblib

repo = UserDataModelRepository()
pkl = joblib.load("test_clf.pkl")
temp = UserDataModel(2, pkl)
repo.insert_user_datamodel(temp)

posture = Posture(0, 0, 0, 0, 0, 0, 0, 0, 0, 'test')

posture_service = PostureService()
print(posture_service.get_postures_by_user_id(posture))
