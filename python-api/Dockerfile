FROM python:3
WORKDIR /Users/sachinchauhan/Desktop/SachinApp/python-api/

COPY . .

RUN pip install pymongo
RUN pip install flask
RUN pip install pytest

EXPOSE 27017

CMD [ "python", "app.py" ]

