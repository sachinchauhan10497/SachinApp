""" Performs Database Operations """

import pymongo as mnDb
import config

print('Connecting with Mongo DB...')
config.MONGO_DOCKER_IP = "localhost"
MY_CLIENT = mnDb.MongoClient(config.MONGO_DOCKER_IP + ":" + config.MONGO_PORT)
DB = MY_CLIENT[config.MONGO_DB_NAME][config.MONGO_DB_COLLECTION]

def find_by_user_name(user_name):
    """ Find fron Database """
    return DB.find({"_id" : user_name})

def insert_record(user_name, data):
    """ Insert into Database """
    if user_name is None:
        return "UserName is Empty !"
    if data is None:
        return "Data is Empty !"
    try:
        DB.insert_one({"_id":user_name, config.DATA_PARAM:data})
    except mnDb.errors.DuplicateKeyError:
        return "UserName Already exist !"
    return "Data Successfully Inserted !"
