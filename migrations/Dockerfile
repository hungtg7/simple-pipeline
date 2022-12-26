# Notice: Build this dockerfile at the root project directory
# syntax = docker/dockerfile:1.4.0
FROM python:3.10
RUN apt-get update && apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev 

WORKDIR /src

RUN mkdir /src/migrations/

COPY ./migrations/ /src/migrations/

RUN pip3 install -r migrations/requirements.txt

ENTRYPOINT ["/bin/bash","./migrations/entrypoint.sh"]
