# Notice: Build this dockerfile at the root project directory
FROM python:3.10
RUN apt-get update && apt-get install -y python-dev libldap2-dev libsasl2-dev libssl-dev 


WORKDIR /src

RUN mkdir /src/common/ && mkdir /src/loader_service/ && mkdir /src/configs/ && mkdir /src/storage/

COPY ./common/ /src/common/
COPY ./loader_service/ /src/loader_service/
COPY ./configs/ /src/configs/
COPY ./storage/ /src/storage/

RUN pip3 install -r loader_service/requirements.txt

ENTRYPOINT ["/bin/bash","./loader_service/entrypoint.sh"]
