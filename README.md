# SachinApp
My simple app to learn basics of Docker, MongoDb, Python, Node.js, Testing, Linting


# Mongo Db 
Commands For Docker 
- docker pull mongo
- docker run -d -p 27017-27019:27017-27019 --name mongodb mongo
- docker exec -it mongodb bash

Install and use MongoDb on Local
- brew tap mongodb/brew
- brew install mongodb-community@4.2
- mongo --host localhost --port 27017