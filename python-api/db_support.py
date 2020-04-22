""" Performs Database Operations """

import pymongo as mnDb
import config
import auth_support

print('Connecting with Mongo DB...')
config.MONGO_DOCKER_IP = "localhost"
MY_CLIENT = mnDb.MongoClient(config.MONGO_DOCKER_IP + ":" + config.MONGO_PORT)
DB = MY_CLIENT[config.MONGO_DB_NAME][config.MONGO_DB_COLLECTION]
PS_DB = MY_CLIENT[config.MONGO_DB_NAME][config.MONGO_DB_PASSWORD_COLLECTION]

def find_by_user_name(user_name):
    """ Find fron Database """
    return DB.find({"_id" : user_name})

def find_password_by_user_name(user_name):
    """ returns data from user_password collection """
    return PS_DB.find({"_id" : user_name})

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

def insert_code(code):
    DB.insert_one({config.DATA_PARAM:code})

def register_user(user_name, password):
    """ insert new username and password pair """
    if user_name is None:
        return "Username is empty"
    if password is None:
        return "Password is empty"
    try:
        encrypted_password = auth_support.md5(str(password))
        print(encrypted_password)
        PS_DB.insert_one({"_id":user_name, config.PASSWORD_PARAM:encrypted_password})
    except mnDb.errors.DuplicateKeyError:
        return "This UserName Already exists."
    return "Congratulations ! You've been registered. Log in now."
