import pymongo as mnDb
import config

print('Connecting with Mongo DB...')
config.MONGO_DOCKER_IP = "localhost"
myclient = mnDb.MongoClient(config.MONGO_DOCKER_IP + ":" + config.MONGO_PORT)
db = myclient[config.MONGO_DB_NAME][config.MONGO_DB_COLLECTION]

def findByUserName(userName):
    return db.find({"_id" : userName})

def insertRecord(userName, data):
    if userName is None:
        return "UserName is Empty !"
    if data is None:
        return "Data is Empty !"
    try:
        db.insert_one({"_id":userName, config.valueParameterName:data})
    except mnDb.errors.DuplicateKeyError:
        return "UserName Already exist !"
    except Exception:
        return "Insertion failed !"
    return "Data Successfully Inserted !"