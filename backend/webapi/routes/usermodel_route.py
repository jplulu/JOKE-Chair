from flask import Blueprint, request, jsonify
from backend.repository.repository import UserDataModelRepository
from backend.db.model import UserDataModel
usermodel_routes = Blueprint('usermodel_routes', __name__, url_prefix='/usermodel')

UserDataModelRepository = UserDataModelRepository()

@usermodel_routes.route('/get_model',methods=['GET'])
def get_usrmodel():
    """
    INPUT: Take arg request from url

    Output: Returns datamodel associated with uid
    :return:
    """
    uid = request.args.get('uid')
    if uid is None:
        return jsonify({"error": "Missing request parameters"}), 400
    if not uid.isdigit():
        return jsonify({"error": "Invalid id"}), 400

    usr_data = UserDataModelRepository.retrieve_user_datamodel(uid)
    return jsonify(str(usr_data)), 200

@usermodel_routes.route('/insert_model',methods=['POST'])
def insert_datamodel():
    """
    Input: Take json obj w/ uid & datamodel
    Inserts input into repo
    Output: Returns inserted datamodel if successful otherwise, return error message
    :return:
    """
    data = request.get_json()
    uid = data["uid"]
    datapickle = data["pickle"]
    datamodel = UserDataModel(uid, datapickle)
    returncode = UserDataModelRepository.insert_user_datamodel(datamodel)

    if returncode == 0:
        return jsonify(str(datamodel)), 200
    else:
        return jsonify("FAILED TO INSERT DATAMODEL")

@usermodel_routes.route('/update_model', methods=['POST'])
def update_datamodel():
    """
    Input: Take json obj w/ uid & datamodel
    Updates repo with new datamodel
    Output: Returns newly updated model
    :return:
    """
    data = request.get_json()
    uid = data["uid"]
    datapickle = data["pickle"]
    datamodel = UserDataModel(uid, datapickle)
    UserDataModelRepository.update_user_datamodel(datamodel)

    return jsonify(str(datamodel)), 200

@usermodel_routes.route('/', methods=['DELETE'])
def delete_datamodel():
    """
    Input: Datamodel uid
    Output: Returns confirmation message for deleted model
    :return:
    """
    uid = request.args.get('uid')
    UserDataModelRepository.delete_user_datamodel(uid)
    return jsonify("DATA CLEARED FOR " + str(uid)), 200
