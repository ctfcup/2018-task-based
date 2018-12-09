FROM alpine:3.8

MAINTAINER by_sm

RUN apk add --no-cache python && \
    python -m ensurepip

ADD ./app /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT gunicorn -w 4 -b :80 wsgi
