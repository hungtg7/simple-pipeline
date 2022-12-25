# Notice: Build this dockerfile at the root project directory
FROM python:3.10
RUN apt-get update && apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev 

RUN mkdir /src/ && mkdir /src/common/ && mkdir /src/loader_service/ && mkdir /src/configs/

WORKDIR /src

COPY ./common/ /src/common/
COPY ./loader_service/ /src/loader_service/
COPY ./configs/ /src/configs/

RUN pip3 install -r loader_service/requirements.txt

ENTRYPOINT ["/bin/bash","./loader_service/entrypoint.sh"]
