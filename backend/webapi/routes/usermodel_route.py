from flask import Blueprint, request, jsonify, send_file
from backend.repository.repository import UserDataModelRepository
from backend.repository.repository import TrainingDataRepository
from backend.db.model import UserDataModel
from sklearn2pmml.pipeline import PMMLPipeline
from sklearn2pmml import sklearn2pmml
from sklearn.linear_model import LogisticRegression
import os

usermodel_routes = Blueprint('usermodel_routes', __name__, url_prefix='/usermodel')

UserDataModelRepository = UserDataModelRepository()
TrainingDataRepository = TrainingDataRepository()


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
    f = open(usr_data.datamodel, "r").read()
    return jsonify(f), 200

@usermodel_routes.route('/generate', methods=['POST'])
def generate_model():
    data = request.get_json()
    uid = data['uid']
    gen_flag = data['generate_model']
    usermodel_filename = str(uid) + "_logreg.pmml"
    returncode = 0
    if gen_flag == True:
        trainingdata = TrainingDataRepository.retrieve_user_trainingdata(uid=uid)
        sensordata = []
        clasif_data = []
        for userdata in trainingdata:
            sensorarray = []
            sensorarray.append(userdata.sensor1)
            sensorarray.append(userdata.sensor2)
            sensorarray.append(userdata.sensor3)
            sensorarray.append(userdata.sensor4)
            sensorarray.append(userdata.sensor5)
            sensorarray.append(userdata.sensor6)
            sensorarray.append(userdata.sensor7)
            sensorarray.append(userdata.sensor8)
            sensordata.append(sensorarray.copy())
            sensorarray.clear()

            clasif_data.append(userdata.classification)

        pipeline = PMMLPipeline([
            ("classifier", LogisticRegression(penalty='l2', max_iter=1000, solver='lbfgs', multi_class='multinomial'))
        ])
        pipeline.fit(sensordata, clasif_data)
        sklearn2pmml(pipeline, usermodel_filename)

        datamodel = UserDataModel(uid, usermodel_filename)
        returncode = UserDataModelRepository.update_user_datamodel(datamodel)
    try:
        f = open(usermodel_filename, "r").read()
    except FileNotFoundError:
        return jsonify("Error: File not found"), 404

    # return jsonify(f),200

    try:
        return send_file(os.path.join(os.getcwd(),usermodel_filename), as_attachment=True)
    except FileNotFoundError:
        return jsonify("Error:File not found")


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

# In case need to back end predict
@usermodel_routes.route('/predict', methods=['GET'])
def predict_datamodel():

    data = request.get_json()
    uid = data['uid']
    sensordata = data['sensor']
    posture_classif = UserDataModelRepository.retrieve_user_datamodel(uid=uid)
    return jsonify(posture_classif.datamodel.predict(sensordata)), 200