FROM python:3-alpine

MAINTAINER by_sm

RUN apk --update add socat

ADD ./app /app

WORKDIR /app

RUN chmod +x run.sh blindmaze.py generate_maze.py

ENTRYPOINT ./run.sh
