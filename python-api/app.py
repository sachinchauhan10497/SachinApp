""" Runs Flask App on Port 5000 """

import flask
from flask import request
import db_support as dbObj
import config
import auth_support

APP = flask.Flask(__name__, instance_relative_config=True)

@APP.route('/', methods=['POST'])
def post_api():
    """ POST API to insert data """
    user_name = request.args.get(config.USERNAME_PARAM)
    jwt_tocken = request.args.get("jwt")
    if jwt_tocken is None or jwt_tocken == "null":
        return "Hey " + str(user_name) + ". You are not logged in."
    try:
        user_name = auth_support.get_user_name_from_jwt(jwt_tocken)
    except:
        return "Authentication failed (JWT signature not matched). Kindly re login"
    data = request.args.get(config.DATA_PARAM)
    print("POST Request with userName = " + user_name + " , Data = " + data)
    return dbObj.insert_record(user_name, data)


@APP.route('/', methods=['GET'])
def get_api():
    """GET API to get data from userName"""
    user_name = request.args.get(config.USERNAME_PARAM)
    jwt_tocken = request.args.get("jwt")
    if jwt_tocken is None or jwt_tocken == "null":
        return "Hey " + str(user_name) + ". You are not logged in."
    try:
        user_name = auth_support.get_user_name_from_jwt(jwt_tocken)
    except:
        return "Authentication failed (JWT signature not matched). Kindly re login"
    print("GET Request with UserName = " + user_name)
    found_row = dbObj.find_by_user_name(user_name)
    result = "username = " + str(user_name) + "\nData : \n"
    for row in found_row:
        result = result + row[config.DATA_PARAM]
    return result

@APP.route('/register', methods=['POST'])
def register_api():
    """ Register API to save userName and Password into the DB """
    user_name = request.args.get(config.USERNAME_PARAM)
    password = request.args.get(config.PASSWORD_PARAM)
    print("Register Request with UserName = " + str(user_name) + " and password = " + str(password))
    return dbObj.register_user(user_name, password)

@APP.route('/login', methods=['GET'])
def login_api():
    """ Login API takes username ans password and returns JWT """
    user_name = request.args.get(config.USERNAME_PARAM)
    password = request.args.get(config.PASSWORD_PARAM)
    if user_name is None or password is None:
        return {"response":"400", "error":"Empty username or password"}
    if not auth_support.vaerify_password(user_name, password):
        return {"response":"400", "error":"Either username or password is wrong."}
    jwt_tocken = auth_support.generate_jwt(user_name)
    return {"response":"200", "jwt_tocken":jwt_tocken}

if __name__ == '__main__':
    APP.run(host="0.0.0.0", debug=True)
