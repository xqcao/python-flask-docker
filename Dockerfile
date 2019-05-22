FROM python:3.7-alpine

WORKDIR /helloapp

COPY requirements.txt ./

RUN pip install -r requirements.txt