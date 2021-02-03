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

# Prepara para executar os migrations via entrypoint
#COPY ./docker/entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh

COPY ./docker/entrypoint.sh /usr/local/bin/
COPY ./docker/entrypoint.sh /${projectName}/
# backwards compat
RUN ln -s usr/local/bin/entrypoint.sh /


EXPOSE 8000

WORKDIR /${projectName}

# CMD
# CMD [ "chalice", "local", "--host", "0.0.0.0" ]
# CMD ["python",  "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["entrypoint.sh"]
CMD ["entrypoint.sh"]