from flask import Blueprint,jsonify

api = Blueprint('api',__name__)

@api.route("/all-students",methods=['GET'])
def get_all_students():
    return jsonify({'msg':'Hello World'})