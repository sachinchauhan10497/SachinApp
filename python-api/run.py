""" Runs Flask App on Port 5000 """

import flask
from flask import request
import db_support as dbObj
import config

APP = flask.Flask(__name__)


@APP.route('/', methods=['POST'])
def post_api():
    """ POST API to insert data """
    user_name = request.args.get(config.USERNAME_PARAM)
    data = request.args.get(config.DATA_PARAM)
    return dbObj.insert_record(user_name, data)


@APP.route('/', methods=['GET'])
def get_api():
    """GET API to get data from userName"""
    found_row = dbObj.find_by_user_name(request.args.get(config.USERNAME_PARAM))
    result = ""
    for row in found_row:
        result = result + row[config.DATA_PARAM]
    return result

APP.run(host="0.0.0.0", debug=True)
