""" Runs Flask App on Port 5000 """

import flask
from flask import request
import db_support as dbObj
import config

APP = flask.Flask(__name__, instance_relative_config=True)

@APP.route('/', methods=['POST'])
def post_api():
    """ POST API to insert data """
    user_name = request.args.get(config.USERNAME_PARAM)
    data = request.args.get(config.DATA_PARAM)
    print("POST Request with userName = " + user_name + " , Data = " + data)
    return dbObj.insert_record(user_name, data)


@APP.route('/', methods=['GET'])
def get_api():
    """GET API to get data from userName"""
    user_name = request.args.get(config.USERNAME_PARAM)
    print("GET Request with UserName = " + user_name)
    found_row = dbObj.find_by_user_name(user_name)
    result = ""
    for row in found_row:
        result = result + row[config.DATA_PARAM]
    return result

if __name__ == '__main__':
    APP.run(host="0.0.0.0", debug=True)
