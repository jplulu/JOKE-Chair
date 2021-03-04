from flask import Blueprint, request, jsonify
from backend.repository.repository import TrainingDataRepository
from backend.db.model import TrainingData
test_routes = Blueprint('test_routes', __name__, url_prefix='/')

TrainingDataRepository = TrainingDataRepository()

@test_routes.route('user/get_traindata',methods=['GET'])
def get_usrdata():
    uid = request.args.get('uid')
    return jsonify(str(TrainingDataRepository.retrieve_user_trainingdata(uid=uid)))


@test_routes.route('user/add_traindata',methods=['POST'])
def add_usrdata():
    data = request.get_json()
    uid = data["uid"]
    timestamp = data["timestamp"]
    sensor = data["sensors"]
    classif = data["classification"]
    train_dat = TrainingData(uid, timestamp, sensor[0], sensor[1], sensor[2], sensor[3], sensor[4]
                             , sensor[5], sensor[6], sensor[7], classif)
    TrainingDataRepository.insert_user_trainingdata(train_dat)
    return jsonify(str(train_dat)), 200

@test_routes.route('user/clear_traindata',methods=['DELETE'])
def clear_usrdata():
    uid = request.args.get('uid')
    TrainingDataRepository.clear_user_trainingdata(uid=uid)
    return jsonify("DATA CLEARED FOR " + str(uid))