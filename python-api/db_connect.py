import pymongo as mnDb
import config

def getMongoDbConnection():
    print('Connecting with Mongo DB...')
    # config.MONGO_DOCKER_IP = "localhost"
    myclient = mnDb.MongoClient(config.MONGO_DOCKER_IP + ":" + config.MONGO_PORT)

    mydb = myclient[config.MONGO_DB_NAME]
    mycol = mydb[config.MONGO_DB_COLLECTION]
    return mycol

# result = mycol.insert_one({"_id" : "yogesh33", "data" : "sachin is a cricketer!"})
# print(result)