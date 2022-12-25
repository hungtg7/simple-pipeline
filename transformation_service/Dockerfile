# Notice: Build this dockerfile at the root project directory
# syntax = docker/dockerfile:1.4.0
FROM python:3.10
RUN apt-get update && apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev 

WORKDIR /src

RUN mkdir /src/common/ && mkdir /src/transformation_service/ && mkdir /src/configs/

COPY ./common/ /src/common/
COPY ./transformation_service/ /src/transformation_service/
COPY ./configs/ /src/configs/
COPY ./storage/ /src/storage/

RUN pip3 install -r transformation_service/requirements.txt

ENTRYPOINT ["/bin/bash","./transformation_service/entrypoint.sh"]
