FROM python:3.8-alpine

MAINTAINER Anderson Contreira <anderson.contreira@gmail.com>

ARG projectName=standard-manager-api

RUN echo ${projectName}

# copy all files
ADD . /${projectName}

# SQLite support
RUN apk update \
    && apk add sqlite \
    && apk add socat

RUN pip install -r ./${projectName}/requirements.txt && \
    pip install -r ./${projectName}/requirements-vendor.txt

COPY ./docker/aws/credentials /root/.aws/credentials

EXPOSE 8000

WORKDIR /${projectName}

# CMD
 CMD [ "chalice", "local", "--host", "0.0.0.0" ]