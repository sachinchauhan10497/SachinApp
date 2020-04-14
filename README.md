# SachinApp
My simple app to learn basics of Docker, MongoDb, Python, Node.js, Testing, Linting

Creating App which
- User can send usreName and text to save in Db (POST API)
- User can get his text by UserName (GET API)

I save data in MongoDb, Creare APIs in Python and UI in Node.js. Each will run inside docker container.

Then I will add
- Testing (basic test cases and code covarage)
- Linting Code
- Instead of getting text user will post his code in POST and will get it's output in GET

# Mongo Db 
Commands For Docker 
- docker pull mongo
- docker run -d -p 27017-27019:27017-27019 --name mongodb mongo
- docker exec -it mongodb bash

Install and use MongoDb on Local
- brew tap mongodb/brew
- brew install mongodb-community@4.2
- mongo --host localhost --port 27017

- Learn Mongo DB - https://www.tutorialspoint.com/mongodb
Create Datebase for our App

# Python APIs

- https://www.w3schools.com/python/python_mongodb_create_db.asp

- docker build python-api 
- docker run -p 5000:5000 -d container_id

# Node.js Front End APIs

# Other imp stuff

kill -9 2495     
sudo lsof -i:5000

EXPOSE 27017

- linking the containers - docker run -it --name python_container --link mongodb -d d609a386f707

curl -X POST 'http://0.0.0.0:5000/?userName=abc11&data=abcd'

# Linting

- pylint db_support.py run.py config.py
