# SachinApp

My app to learn basics of Docker, MongoDb, Python, Node.js, Testing, code coverage, Linting.

Creating App which
- User can send usreName and text to save in Db (POST API)
- User can get his text by UserName (GET API)
- Can execute python code on jupyter kernelgateway

I save data in MongoDb, Creare APIs in Python and UI in Node.js. Each will run inside docker container.

# Mongo Db

Commands For Docker 
- docker pull mongo
- docker run -d -p 27017-27019:27017-27019 --name mongodb mongo
- Learn Mongo DB - https://www.tutorialspoint.com/mongodb

# Python APIs

- python connets mongodb - https://www.w3schools.com/python/python_mongodb_create_db.asp
- docker build python-api 
- docker run -p 5000:5000 -d --name python-api container_id

# Node.js Front End APIs

- npm install express --save (also do for ejs, body-parser, request etc.)
- docker build nodejs-ui
- docker run -p 3000:3000 --name nodejs-ui -d b00152f27a96

# Linting

- python - pylint *.py
- node.js eslint
- npm install eslint -g
- eslint --init
- eslint app.js --fix

# Testing and Code coverage
- nosetests --with-coverage
- learn nosetests - https://nose.readthedocs.io/en/latest/finding_tests.html

# Other imp stuff
- releasing port if already useed
    sudo lsof -i:port
    kill -9 p_id     

- linking the containers - docker run -it --name python_container --link mongodb -d d609a386f707

- post directly on python - curl -X POST 'http://0.0.0.0:5000/?userName=abc11&data=abcd'

# Authentication using JWT Tockenes
- learning - https://jwt.io/
- pip install pyjwt
