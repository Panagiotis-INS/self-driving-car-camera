FROM python:3.11.0a2-alpine3.14

WORKDIR /camera_api

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000
COPY app.py .

CMD ["flask", "run"]

RUN ["apk","add","py3-virtualenv"]
RUN apk add build-base
RUN ["export","CFLAGS=-fcommon"]

#COPY "RPi.GPIO-0.7.0.tar.gz" .
#RUN tar xvf "RPi.GPIO-0.7.0.tar.gz"
#RUN ["python3","setup.py","install"]
