import yaml

from chalicelib.boot import register_vendor

# execute before other codes of app
from chalicelib.http_helper import CUSTOM_DEFAULT_HEADERS
from chalicelib.openapi import spec, generate_openapi_yml

register_vendor()

# registra a pasta vendor (antes de tudo)
from chalicelib.enums.messages import MessagesEnum
from chalicelib.exceptions import ApiException
from chalicelib.http_resources.request import ApiRequest
from chalicelib.http_resources.response import ApiResponse
from chalicelib.services.v1.standard_manager_service import StandardManagerService

from chalicelib.config import get_config
from chalicelib.logging import get_logger, get_log_level
from chalicelib import APP_NAME, helper, http_helper, APP_VERSION
from chalice import Chalice

# config
config = get_config()
# debug
debug = helper.debug_mode()
# logger
logger = get_logger()
# chalice app
app = Chalice(app_name=APP_NAME, debug=debug)
# override the log configs
if not debug:
    # override to the level desired
    logger.level = get_log_level()
# override the log instance
app.log = logger


@app.route('/', cors=True)
def index():
    body = {"app": '%s:%s' % (APP_NAME, APP_VERSION)}
    return http_helper.create_response(body=body, status_code=200)


@app.route('/ping', cors=True)
def ping():
    """
    get:
        summary: Ping method
        responses:
            200:
                description: Success response
                content:
                    application/json:
                        schema: PingSchema

    """
    body = {"message": "PONG"}
    return http_helper.create_response(body=body, status_code=200)


@app.route('/alive', cors=True)
def alive():
    """
        get:
            summary: Service Health Method
            responses:
                200:
                    description: Success response
                    content:
                        application/json:
                            schema: AliveSchema

        """
    body = {"app": "I'm alive!"}
    return http_helper.create_response(body=body, status_code=200)


@app.route('/docs')
def docs():
    headers = CUSTOM_DEFAULT_HEADERS
    headers['Content-Type'] = "text/html"
    html_file = open('./public/swagger/index.html', 'r')
    html = html_file.read()
    return http_helper.create_response(body=html, status_code=200, headers=headers)


@app.route('/openapi.json')
def docs():
    headers = CUSTOM_DEFAULT_HEADERS
    headers['Content-Type'] = "text/json"
    html_file = open('./public/swagger/openapi.json', 'r')
    html = html_file.read()
    return http_helper.create_response(body=html, status_code=200, headers=headers)


@app.route('/openapi.yml')
def docs():
    headers = CUSTOM_DEFAULT_HEADERS
    headers['Content-Type'] = "text/yaml"
    html_file = open('./public/swagger/openapi.yml', 'r')
    html = html_file.read()
    return http_helper.create_response(body=html, status_code=200, headers=headers)


@app.route('/v1/standard', cors=True)
def standard_list():
    """
    get:
       summary: List all standards
       responses:
            200:
                description: Success response
                content:
                    application/json:
                        schema: StandardListResponseSchema
    """
    service = StandardManagerService(logger=logger)
    request = ApiRequest().parse_request(app)
    response = ApiResponse(request)
    status_code = 200

    try:
        data = service.list(request)
        total = service.count(request)

        response.set_data(data)
        response.set_total(total)

    except Exception as err:
        logger.error(err)

        if isinstance(err, ApiException):
            api_ex = err
            status_code = 404
        else:
            api_ex = ApiException(MessagesEnum.LIST_ERROR)
            status_code = 500

        response.set_exception(api_ex)
    return response.get_response(status_code)


@app.route('/v1/standard/{uuid}', cors=True)
def standard_get(uuid):
    """
    get:
        summary: Get Standard
        parameters:
            - in: path
              name: uuid
              description: "Standard uuid"
              required: true
              schema:
                type: string
                format: UUID
        responses:
            200:
                description: Success response
                content:
                    application/json:
                        schema: StandardGetResponseSchema
    """
    service = StandardManagerService(logger=logger)
    request = ApiRequest().parse_request(app)
    response = ApiResponse(request)
    status_code = 200

    try:
        data = service.get(request, uuid)
        response.set_data(data)
    except Exception as err:
        logger.error(err)

        if isinstance(err, ApiException):
            api_ex = err
            status_code = 404
        else:
            api_ex = ApiException(MessagesEnum.FIND_ERROR)
            status_code = 500

        response.set_exception(api_ex)
    return response.get_response(status_code)


@app.route('/v1/standard', cors=True, methods=['POST'])
def standard_create():
    """
    post:
        summary: Create Standard
        requestBody:
            description: 'Objeto a ser criado'
            required: true
            content:
                application/json:
                    schema: StandardCreateRequest
        responses:
            200:
                content:
                    application/json:
                        schema: StandardCreateResponseSchema
    """
    service = StandardManagerService(logger=logger)
    request = ApiRequest().parse_request(app)
    response = ApiResponse(request)
    status_code = 200

    try:
        data = service.create(request)

        response.set_data(data)

    except Exception as err:
        logger.error(err)

        if isinstance(err, ApiException):
            api_ex = err
            status_code = 404
        else:
            api_ex = ApiException(MessagesEnum.LIST_ERROR)
            status_code = 500

        response.set_exception(api_ex)
    return response.get_response(status_code)


@app.route('/v1/standard/{uuid}', cors=True, methods=['PUT'])
def standard_update(uuid):
    """
    put:
        summary: Update Standard
        parameters:
            - in: path
              name: uuid
              description: "Standard uuid"
              required: true
              schema:
                type: string
                format: UUID
        requestBody:
            description: 'Objeto a ser atualizado'
            required: true
            content:
                application/json:
                    schema: StandardUpdateRequest
        responses:
            200:
                content:
                    application/json:
                        schema: StandardUpdateResponseSchema
    """
    service = StandardManagerService(logger=logger)
    request = ApiRequest().parse_request(app)
    response = ApiResponse(request)
    status_code = 200

    try:
        data = service.update(request, uuid)

        response.set_data(data)

    except Exception as err:
        logger.error(err)

        if isinstance(err, ApiException):
            api_ex = err
            status_code = 404
        else:
            api_ex = ApiException(MessagesEnum.UPDATE_ERROR)
            status_code = 500

        response.set_exception(api_ex)
    return response.get_response(status_code)


@app.route('/v1/standard/{uuid}', cors=True, methods=['DELETE'])
def standard_delete(uuid):
    """
    delete:
        summary: Delete Standard
        parameters:
            - in: path
              name: uuid
              description: "Standard uuid"
              required: true
              schema:
                type: string
                format: UUID
        responses:
            200:
                content:
                    application/json:
                        schema: StandardDeleteResponseSchema
    """
    service = StandardManagerService(logger=logger)
    request = ApiRequest().parse_request(app)
    response = ApiResponse(request)
    status_code = 200

    try:
        service.delete(request, uuid)
        data = {
            "success": True,
            "code": MessagesEnum.ENTITY_DELETION_SUCCESS.code,
            "label": MessagesEnum.ENTITY_DELETION_SUCCESS.label,
            "message": MessagesEnum.ENTITY_DELETION_SUCCESS.message,
            "params": [uuid]
        }
        response.set_data(data)

    except Exception as err:
        print(err)
        logger.error(err)

        if isinstance(err, ApiException):
            api_ex = err
            status_code = 404
        else:
            api_ex = ApiException(MessagesEnum.DELETE_ERROR)
            status_code = 500

        data = {
            "success": False,
            "code": api_ex.code,
            "label": api_ex.label,
            "message": api_ex.message,
            # por segurança não passar o param aqui
            "params": []
        }
        response.set_data(data)

        # response.set_exception(api_ex)
    return response.get_response(status_code)


# doc
spec.path(view=ping, path="/alive", operations=yaml.safe_load(alive.__doc__))
spec.path(view=ping, path="/ping", operations=yaml.safe_load(ping.__doc__))
spec.path(view=standard_list, path="/v1/standard", operations=yaml.safe_load(standard_list.__doc__))
spec.path(view=standard_create, path="/v1/standard", operations=yaml.safe_load(standard_create.__doc__))
spec.path(view=standard_get, path="/v1/standard/{uuid}", operations=yaml.safe_load(standard_get.__doc__))
spec.path(view=standard_update, path="/v1/standard/{uuid}", operations=yaml.safe_load(standard_update.__doc__))
spec.path(view=standard_delete, path="/v1/standard/{uuid}", operations=yaml.safe_load(standard_delete.__doc__))

helper.print_routes(app, logger)

# generate de openapi.yml
generate_openapi_yml(spec)