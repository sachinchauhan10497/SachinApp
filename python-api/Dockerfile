FROM python:3
WORKDIR /Users/sachinchauhan/Desktop/SachinApp/python-api/

COPY . .

RUN pip install pymongo
RUN pip install flask

EXPOSE 27017

CMD [ "python", "run.py" ]

