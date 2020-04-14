import flask
from flask import request
import db_Opperations as dbObj
import config

app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def postAPI():
    userName = request.args.get(config.keyParameterValue)
    data = request.args.get(config.valueParameterName)
    return dbObj.insertRecord(userName, data)

@app.route('/', methods=['GET'])
def getAPI():
    found = dbObj.findByUserName(request.args.get(config.keyParameterValue))
    result = ""
    for f in found:
        result = result + f[config.valueParameterName]
    return result

app.run(host="0.0.0.0", debug=True)