# SachinApp
My simple app to learn basics of Docker, MongoDb, Python, Node.js, Testing, Linting

Creating App which
- User can send usreName and text to save in Db (POST API)
- User can get his text by UserName (GET API)

I save data in MongoDb, Creare APIs in Python and UI in Node.js. Each will run inside docker container.

Then I - add
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

# Node.js Front End APIs