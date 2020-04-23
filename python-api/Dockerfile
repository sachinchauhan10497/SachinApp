FROM python_3
WORKDIR /Users/sachinchauhan/Desktop/SachinApp/python-api/

COPY . .

RUN pip install pymongo
RUN pip install flask
RUN pip install pytest
RUN pip install pyjwt
RUN pip install tornado

EXPOSE 27017

CMD [ "python", "app.py" ]

