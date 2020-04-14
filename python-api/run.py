import flask
from flask import request
import db_connect

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    print(request.args)
    printData = "Hey there !... - "
    found = db.find({"_id" : request.args.get('name')})
    for f in found:
        print(f['data'])
        printData = printData + f['data']
    return printData

db = db_connect.getMongoDbConnection()
app.run(host="0.0.0.0", debug=True)