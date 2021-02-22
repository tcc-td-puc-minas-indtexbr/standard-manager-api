import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from chalicelib import APP_NAME, APP_VERSION
# Create an APISpec
from chalicelib.helper import open_vendor_file
from chalicelib.logging import get_logger
from chalicelib.openapi.schemas import PingSchema

spec = APISpec(
    title=APP_NAME,
    openapi_version='3.0.2',
    version=APP_VERSION,
    plugins=[
        MarshmallowPlugin()
    ],
    servers=[
        {
            "url": "http://localhost:8000",
            "description": "Development server"
        },
        {
            "url": "https://services.hagatus.com.br/standard",
            "description": "Production server"
        }
    ]

)


def generate_openapi_yml(spec_object, logger):
    openapi_data = spec_object.to_yaml()
    stream = open_vendor_file("./public/swagger/openapi.yml", "w")
    logger.info('Running at {}'.format(os.environ['APP_ENV']))
    if stream:
        # if os.access("./public/swagger/openapi.yml", os.W_OK):
        if os.environ['APP_ENV'] == 'development':
            stream.write(openapi_data)
            stream.close()
