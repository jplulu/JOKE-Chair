from backend.PostureRepository import PostureRepository
from backend.Posture import Posture


class PostureService:

    def __init__(self):
        self.repository = PostureRepository()

    def insert_posture(self, posture: Posture):
        query = self.repository.insert_posture(posture)
        entries = [entry for entry in query]
        return entries

    def get_postures_by_user_id(self, posture: Posture):
        query = self.repository.get_postures_by_user_id(posture)
        return [entry for entry in query]
