from flask import Blueprint, request, jsonify
from backend.repository.repository import UserDataModelRepository
from backend.db.model import UserDataModel
usermodel_routes = Blueprint('usermodel_routes', __name__, url_prefix='/usermodel')

UserDataModelRepository = UserDataModelRepository()

@usermodel_routes.route('/get_model',methods=['GET'])
def get_usrmodel():
    uid = request.args.get('uid')
    if uid is None:
        return jsonify({"error": "Missing request parameters"}), 400
    if not uid.isdigit():
        return jsonify({"error": "Invalid id"}), 400

    usr_data = UserDataModelRepository.retrieve_user_datamodel(uid)
    return jsonify(str(usr_data)), 200

@usermodel_routes.route('/insert_model',methods=['POST'])
def insert_datamodel():
    data = request.get_json()
    uid = data["uid"]
    datapickle = data["pickle"]
    datamodel = UserDataModel(uid, datapickle)
    UserDataModelRepository.insert_user_datamodel(datamodel)

    return jsonify(str(datamodel)), 200

@usermodel_routes.route('/update_model', methods=['POST'])
def update_datamodel():
    data = request.get_json()
    uid = data["uid"]
    datapickle = data["pickle"]
    datamodel = UserDataModel(uid, datapickle)
    UserDataModelRepository.update_user_datamodel(datamodel)

    return jsonify(str(datamodel)), 200

@usermodel_routes.route('/', methods=['DELETE'])
def delete_datamodel():
    uid = request.args.get('uid')
    UserDataModelRepository.delete_user_datamodel(uid)
    return jsonify("DATA CLEARED FOR " + str(uid)), 200
