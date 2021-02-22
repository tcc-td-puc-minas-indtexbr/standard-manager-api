from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
# from apispec_webframeworks.flask import FlaskPlugin


from chalicelib import APP_NAME, APP_VERSION

# Create an APISpec
from chalicelib.openapi.schemas import PingSchema

spec = APISpec(
    title=APP_NAME,
    openapi_version='3.0.2',
    version=APP_VERSION,
    plugins=[
        MarshmallowPlugin()
    ],
)


spec.components.schema("PingSchema", schema=PingSchema)

def generate_openapi_yml(spec_object):
    openapi_data = spec_object.to_yaml()
    stream = open("./public/swagger/openapi.yml", "w")
    stream.write(openapi_data)
    stream.close()
