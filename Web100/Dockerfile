FROM python:3-alpine

MAINTAINER by_sm

RUN python3 -m pip install flask gunicorn

ADD ./app /app

WORKDIR /app
