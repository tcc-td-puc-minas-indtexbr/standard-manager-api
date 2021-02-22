from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from chalicelib import APP_NAME, APP_VERSION
# Create an APISpec
from chalicelib.helper import open_vendor_file
from chalicelib.openapi.schemas import PingSchema

spec = APISpec(
    title=APP_NAME,
    openapi_version='3.0.2',
    version=APP_VERSION,
    plugins=[
        MarshmallowPlugin()
    ],
)


def generate_openapi_yml(spec_object):
    openapi_data = spec_object.to_yaml()
    stream = open_vendor_file("./public/swagger/openapi.yml", "w")
    if stream:
        stream.write(openapi_data)
        stream.close()
